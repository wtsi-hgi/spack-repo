from spack.package import *


class Stduuid(CMakePackage):
    """A C++17 cross-platform UUID library."""

    homepage = "https://github.com/mariusbancila/stduuid"
    url = "https://github.com/mariusbancila/stduuid/archive/refs/tags/v1.2.3.tar.gz"

    license("MIT")

    version("1.2.3", sha256="b1176597e789531c38481acbbed2a6894ad419aab0979c10410d59eb0ebf40d3")

    depends_on("cmake@3.14:", type="build")

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            test_source = "test.cpp"
            with open(test_source, "w", encoding="utf-8") as f:
                f.write("#include <random>\n#include <uuid.h>\nint main() { std::mt19937 gen(123); auto u = uuids::uuid_random_generator{gen}(); return u.as_bytes().size() == 16 ? 0 : 1; }\n")
            cxx = which(self.compiler.cxx)
            cxx(test_source, "-I", self.prefix.include, "-o", "test-stduuid")
            Executable("./test-stduuid")()
