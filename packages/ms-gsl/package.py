from spack.package import *


class MsGsl(CMakePackage):
    """Microsoft Guidelines Support Library."""

    homepage = "https://github.com/microsoft/GSL"
    url = "https://github.com/microsoft/GSL/archive/refs/tags/v4.1.0.tar.gz"

    license("MIT")

    version("4.1.0", sha256="0a227fc9c8e0bf25115f401b9a46c2a68cd28f299d24ab195284eb3f1d7794bd")

    depends_on("cmake@3.14:", type="build")

    def cmake_args(self):
        return [self.define("GSL_TEST", False)]

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            test_source = "test.cpp"
            with open(test_source, "w", encoding="utf-8") as f:
                f.write("#include <gsl/pointers>\nint main() { int x = 1; gsl::not_null<int*> p(&x); return *p - 1; }\n")
            cxx = which(self.compiler.cxx)
            cxx(test_source, "-I", self.prefix.include, "-o", "test-gsl")
            Executable("./test-gsl")()
