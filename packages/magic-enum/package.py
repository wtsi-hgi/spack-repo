from spack.package import *


class MagicEnum(CMakePackage):
    """Static reflection for enums in modern C++."""

    homepage = "https://github.com/Neargye/magic_enum"
    url = "https://github.com/Neargye/magic_enum/archive/refs/tags/v0.9.7.tar.gz"

    license("MIT")

    version("0.9.7", sha256="b403d3dad4ef542fdc3024fa37d3a6cedb4ad33c72e31b6d9bab89dcaf69edf7")

    depends_on("cmake@3.14:", type="build")

    def cmake_args(self):
        return [self.define("MAGIC_ENUM_OPT_BUILD_TESTS", False)]

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            test_source = "test.cpp"
            with open(test_source, "w", encoding="utf-8") as f:
                f.write("#include <magic_enum/magic_enum.hpp>\nenum class Color { Red, Green };\nint main() { return magic_enum::enum_name(Color::Red) == \"Red\" ? 0 : 1; }\n")
            cxx = which(self.compiler.cxx)
            cxx(test_source, "-I", self.prefix.include, "-o", "test-magic-enum")
            Executable("./test-magic-enum")()
