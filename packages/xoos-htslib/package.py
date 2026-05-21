from spack.package import *


class XoosHtslib(AutotoolsPackage):
    """HTSlib packaged with the CMake target name expected by XOOS."""

    homepage = "https://www.htslib.org"
    url = "https://github.com/samtools/htslib/releases/download/1.21/htslib-1.21.tar.bz2"

    license("MIT")

    version("1.21", sha256="84b510e735f4963641f26fd88c8abdee81ff4cb62168310ae716636aac0f1823")

    depends_on("zlib-ng+compat", type=("build", "link", "run"))
    depends_on("bzip2", type=("build", "link", "run"))
    depends_on("xz", type=("build", "link", "run"))
    depends_on("libdeflate", type=("build", "link", "run"))
    depends_on("curl", type=("build", "link", "run"))

    def configure_args(self):
        return ["--with-libdeflate", "--enable-libcurl"]

    def setup_build_environment(self, env):
        env.prepend_path("CPATH", self.spec["zlib-ng"].prefix.include)
        env.prepend_path("LIBRARY_PATH", self.spec["zlib-ng"].prefix.lib)

    def install(self, spec, prefix):
        super().install(spec, prefix)
        cfgdir = prefix.lib.cmake.join("xoos-htslib")
        mkdirp(cfgdir)
        with open(cfgdir.join("xoos-htslib-config.cmake"), "w", encoding="utf-8") as f:
            f.write(
                'add_library(xoos-htslib::xoos-htslib SHARED IMPORTED)\n'
                'set_target_properties(xoos-htslib::xoos-htslib PROPERTIES\n'
                '  IMPORTED_LOCATION "${CMAKE_CURRENT_LIST_DIR}/../../../lib/libhts.so"\n'
                '  INTERFACE_INCLUDE_DIRECTORIES "${CMAKE_CURRENT_LIST_DIR}/../../../include"\n'
                '  INTERFACE_LINK_LIBRARIES "zlib;${CMAKE_DL_LIBS}"\n'
                ')\n'
            )

    @run_after("install")
    def install_test(self):
        htsfile = Executable(join_path(self.prefix.bin, "htsfile"))
        htsfile("--help")
