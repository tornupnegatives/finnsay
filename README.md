# Finnsay

Finnsay is cowsay clone featuring Finn the Human, from the Cartoon Network show
Adventure Time.

## Usage

You can pass Finnsay a string:

```shell
$ finnsay "Hello world"
/-------------\
| Hello world|
\-------------/
        \    ***                 ***
         \  *   *  ***********  *   *
          \ *   ***          ** *   *
           \*      .---------.      *
            *  _.-'           `--.  *
            * /                   \ *
            *;     *         *     :*
            *:                     ;*
            * \     *********     / *
            *  \                 /  *
            *   `--.         _.-'   *
            *       `-------'       *
             ***********************
```

Or you can send data to Finnsay using a pipe:

```shell
$ fortune | finnsay
/-------------------------------------------\
| Fudd's First Law of Opposition:         |
| Push something hard enough and it will  |
| fall over.                              |
\-------------------------------------------/
        \    ***                 ***
         \  *   *  ***********  *   *
          \ *   ***          ** *   *
           \*      .---------.      *
            *  _.-'           `--.  *
            * /                   \ *
            *;     *         *     :*
            *:                     ;*
            * \     *********     / *
            *  \                 /  *
            *   `--.         _.-'   *
            *       `-------'       *
             ***********************
```
