from spack.package import *

import os


class XoosLightgbm(CMakePackage):
    """LightGBM packaged with the CMake target name expected by XOOS."""

    homepage = "https://github.com/lightgbm-org/LightGBM"
    url = "file:///mnt/data/softpack-agent/tmp/xoos-work/lightgbm-full-v4.6.0-with-submodules.tar.gz"

    license("MIT")

    version("4.6.0", sha256="b05ecefd290097670f7a58499849ad5e464b3685750e10a7f560c3b936673934")

    depends_on("cmake@3.28:", type="build")
    depends_on("eigen")
    depends_on("fmt")

    def patch(self):
        include_dir = join_path(self.stage.source_path, "external_libs", "fast_double_parser", "include")
        mkdirp(include_dir)
        if not os.path.exists(join_path(include_dir, "fast_double_parser.h")):
            curl = which("curl")
            curl(
                "-L",
                "-o",
                join_path(include_dir, "fast_double_parser.h"),
                "https://raw.githubusercontent.com/lemire/fast_double_parser/v0.8.0/include/fast_double_parser.h",
            )
        filter_file(
            'set(EIGEN_DIR "${PROJECT_SOURCE_DIR}/external_libs/eigen")',
            'set(EIGEN_DIR "{0}")'.format(self.spec["eigen"].prefix.include.eigen3),
            join_path(self.stage.source_path, "CMakeLists.txt"),
            string=True,
        )
        filter_file(
            'set(FMT_INCLUDE_DIR "${PROJECT_SOURCE_DIR}/external_libs/fmt/include")',
            'set(FMT_INCLUDE_DIR "{0}")'.format(self.spec["fmt"].prefix.include),
            join_path(self.stage.source_path, "CMakeLists.txt"),
            string=True,
        )

    def cmake_args(self):
        return [
            self.define("BUILD_CPP_TEST", False),
            self.define("BUILD_CLI", False),
            self.define("BUILD_STATIC_LIB", True),
            self.define("USE_GPU", False),
            self.define("USE_CUDA", False),
            self.define("USE_MPI", False),
            self.define("USE_OPENMP", True),
            self.define("INSTALL_HEADERS", True),
        ]

    def install(self, spec, prefix):
        super().install(spec, prefix)
        mkdirp(join_path(prefix.include, "LightGBM", "utils"))
        install(
            join_path(self.stage.source_path, "external_libs", "fast_double_parser", "include", "fast_double_parser.h"),
            join_path(prefix.include, "LightGBM", "utils"),
        )
        cfgdir = prefix.lib.cmake.join("xoos-lightgbm")
        mkdirp(cfgdir)
        with open(cfgdir.join("xoos-lightgbm-config.cmake"), "w", encoding="utf-8") as f:
            f.write(
                'include("${CMAKE_CURRENT_LIST_DIR}/../LightGBM/LightGBMTargets.cmake")\n'
                'if(TARGET _lightgbm AND NOT TARGET xoos-lightgbm::xoos-lightgbm)\n'
                '  add_library(xoos-lightgbm::xoos-lightgbm ALIAS _lightgbm)\n'
                'endif()\n'
            )

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            test_source = "test.cpp"
            with open(test_source, "w", encoding="utf-8") as f:
                f.write("#include <LightGBM/c_api.h>\nint main() { return LGBM_GetLastError() ? 0 : 0; }\n")
            cxx = which(self.compiler.cxx)
            cxx(
                test_source,
                "-I",
                self.prefix.include,
                "-L",
                self.prefix.lib,
                "-Wl,-rpath," + self.prefix.lib,
                "-fopenmp",
                "-l_lightgbm",
                "-o",
                "test-lightgbm",
            )
            Executable("./test-lightgbm")()
