from spack.package import *


class VincentlaucsbCsvParser(CMakePackage):
    """A fast CSV parser and serializer for modern C++."""

    homepage = "https://github.com/vincentlaucsb/csv-parser"
    url = "https://github.com/vincentlaucsb/csv-parser/archive/refs/tags/2.3.0.tar.gz"

    license("MIT")

    version("2.3.0", sha256="27b8ac51aa58b9a4debd8ccfb44738c8583a2e874da42f56bbdf3764b75f3af5")

    depends_on("cmake@3.9:", type="build")

    def cmake_args(self):
        return [
            self.define("CSV_BUILD_PROGRAMS", False),
            self.define("CSV_DEVELOPER", False),
            self.define("BUILD_PYTHON", False),
        ]

    def install(self, spec, prefix):
        cmake(".", *self.std_cmake_args)
        make("csv")
        mkdirp(prefix.include)
        install_tree("include", prefix.include)
        mkdirp(prefix.lib)
        install(join_path("include", "internal", "libcsv.a"), prefix.lib)
        cfgdir = prefix.lib.cmake.join("vincentlaucsb-csv-parser")
        mkdirp(cfgdir)
        with open(join_path(cfgdir, "vincentlaucsb-csv-parser-config.cmake"), "w", encoding="utf-8") as f:
            f.write(
                'add_library(vincentlaucsb-csv-parser::vincentlaucsb-csv-parser STATIC IMPORTED)\n'
                'set_target_properties(vincentlaucsb-csv-parser::vincentlaucsb-csv-parser PROPERTIES\n'
                '  IMPORTED_LOCATION "${CMAKE_CURRENT_LIST_DIR}/../../../lib/libcsv.a"\n'
                '  INTERFACE_INCLUDE_DIRECTORIES "${CMAKE_CURRENT_LIST_DIR}/../../../include"\n'
                ')\n'
            )

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            test_source = "test.cpp"
            with open(test_source, "w", encoding="utf-8") as f:
                f.write("#include <csv.hpp>\nint main() { csv::CSVFormat format; return 0; }\n")
            cxx = which(self.compiler.cxx)
            cxx(test_source, "-I", self.prefix.include, "-L", self.prefix.lib, "-lcsv", "-o", "test-csv")
            Executable("./test-csv")()
