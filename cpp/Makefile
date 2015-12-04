CC=clang++
CXXFLAGS=-Wall -Wextra -Werror -pedantic -std=c++0x
SRC=format.cc
OBJS=$(SRC:.cc=.o)
BIN=format

all: ${BIN}

${BIN}: ${OBJS}
	${CC} ${CXXFLAGS} $^ -o $@

clean:
	rm ${OBJS} ${BIN}
