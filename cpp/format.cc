#include "format.hh"

int usage(void);
char *getOption(char **begin, char **end, const std::string &option);
bool optionExist(char **begin, char **end, const std::string &option);
doc readFile(std::string filename);


int main(int argc, char **argv)
{
  if (optionExist(argv, argv + argc, "-h") or argc == 1)
      return usage();

  char *input = getOption(argv, argv + argc, "-i");
  char *output = getOption(argv, argv + argc, "-o");


  std::ofstream ofs;
  ofs.open(output);

  doc d = readFile(input);

  auto idf_dict = idf(d);
  auto dict = std::make_shared<std::map<std::string, float>>();
  float tf_val;
  for (auto it = d->begin(); it != d->end(); ++it)
    for (auto jt = (*it)->tokens.begin(); jt != (*it)->tokens.end(); ++jt)
      (*dict)[*jt] = 0;
  for (auto it = d->begin(); it != d->end(); ++it)
  {
    for (auto jt = (*it)->tokens.begin(); jt != (*it)->tokens.end(); ++jt)
    {
      tf_val = tf(*it, *jt);
      if ((*idf_dict)[*jt])
        (*dict)[*jt] = tf_val / (*idf_dict)[*jt];
    }
    ofs << (*it)->grade;
    int i = 1;
    for(const auto &myPair : (*dict))
    {
      std::cout << myPair.first << std::endl;
      if (myPair.second)
        ofs << " " << i << ":" << myPair.second;
      ++i;
    }
    ofs << std::endl;
  }

  return EXIT_SUCCESS;
}

int usage(void)
{
  using namespace std;
  cout << "Usage:" << endl << "\t" << "format -i <input> -o <output>" << endl;
  return EXIT_FAILURE;
}

char *getOption(char **begin, char **end, const std::string &option)
{
  auto itr = std::find(begin, end, option);
  if (itr != end and ++itr != end)
    return *itr;
  return nullptr;
}

bool optionExist(char **begin, char **end, const std::string &option)
{
  return std::find(begin, end, option) != end;
}

doc readFile(std::string filename)
{
  std::ifstream ifs;
  ifs.open(filename);
  doc d = std::make_shared<std::vector<s_line>>();

  std::string line;
  while (std::getline(ifs, line))
  {
    int tab = line.find('\t', 0);
    int grade = std::stoi(line.substr(0,tab));
    std::cout << line << std::endl;
    line = line.substr(tab + 1, line.size());
    auto b = bigrams(line);
    b->grade = grade;
    d->push_back(b);
    /*std::cout << "[ ";
    for (auto jt = b->tokens.begin(); jt != b->tokens.end(); ++jt)
      std::cout << *jt << ", ";
    std::cout << " ]" << std::endl;*/
  }
  return d;
}
s_line bigrams(std::string l)
{
  s_line v = std::make_shared<line>();
  size_t pos = 0;
  size_t next = 0;
  while (next != std::string::npos)
  {
    next = l.find(' ', pos);
    v->tokens.push_back(l.substr(pos, (next == std::string::npos) ?
                             std::string::npos : next - pos));
    pos = next + 1;
  }
  auto end = v->tokens.end();
  vector_s vs;
  for (auto it = v->tokens.begin(); it + 1 != end; ++it)
  {
    vs.push_back(*it + '_' + *(it + 1));
    std::cout << "Bigram : " <<  *it << "_" << *(it + 1) << std::endl;
  }
  for (auto it = vs.begin(); it != vs.end(); ++it)
    v->tokens.push_back(*it);
  return v;
}

s_map idf(doc d)
{
  s_map m = std::make_shared<map_s_f>();
  for (auto it = d->begin(); it != d->end(); ++it)
    for (auto jt = (*it)->tokens.begin(); jt != (*it)->tokens.end(); ++jt)
    {
      int i = 0;
      for (auto kt = d->begin(); kt != d->end(); ++kt)
      {
        if (kt == it)
          continue;
        if (std::find((*kt)->tokens.begin(), (*kt)->tokens.end(), *jt) != (*kt)->tokens.end())
          ++i;
      }
      (*m)[*jt] = i ? log10(i / (d->end() - d->begin())) : 0;
    }
  return m;
}

float tf(s_line& sv, std::string word)
{
  int i = 0;
  for (auto it = sv->tokens.begin(); it != sv->tokens.end(); ++it)
    if (*it == word)
      ++i;
  return (i / (sv->tokens.end() - sv->tokens.begin()));
}
