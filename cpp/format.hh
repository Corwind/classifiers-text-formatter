#ifndef TFIDF_HH

  #define TFIDF_HH
  #include <fstream>
  #include <memory>
  #include <vector>
  #include <map>
  #include <unordered_map>
  #include <string>
  #include <algorithm>
  #include <iostream>
  #include <cstdlib>

  using map_s_f = std::map<std::string, float>;
  using s_map = std::shared_ptr<map_s_f>;
  using umap_s_f = std::unordered_map<std::string, float>;
  using s_umap = std::shared_ptr<umap_s_f>;
  using vector_s = std::vector<std::string>;
  class line {
    public:
    int grade;
    vector_s tokens;
    line()
      :grade(), tokens()
    {}
    ~line()
    {}
  };
  using s_line = std::shared_ptr<line>;
  using doc = std::shared_ptr<std::vector<s_line>>;

  s_line bigrams(std::string line);
  s_map idf(doc d);
  float tf(s_line& sv, std::string word);


#endif
