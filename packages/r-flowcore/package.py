# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
import os


class RFlowcore(RPackage):
    """flowCore: Basic structures for flow cytometry data

    Provides S4 data structures and basic functions to deal with flow cytometry data.
    """

    bioc = "flowCore"

    version("2.20.0", commit="c75a5ca6386037eb7fb226d3abf6f855da9a1020")
    version("2.14.2", commit="45da1bc14efd253d9812d6260e9f0d5b6a30c7de")
    version("2.14.1", md5="29b7b1bbecfbd24824f7ec4334a5e640")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-biocgenerics@0.29.2:", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-matrixstats", type=("build", "run"))
    depends_on("r-cytolib", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-cpp11", type=("build", "run"))
    depends_on("r-bh@1.81:", type=("build", "run"))
    depends_on("r-rprotobuflib", type=("build", "run"))

    # Required at link time because flowCore links against cytolib's static
    # library which depends on Boost filesystem/system symbols.
    depends_on("boost@1.72:+filesystem+system cxxstd=17", type=("link"))

    def setup_build_environment(self, env):
        # Ensure Boost libraries are linked when building shared object
        # so that symbols from Boost.Filesystem/System are resolved.
        if "+filesystem" in self.spec["boost"]:
            boost_ldflags = self.spec["boost"].libs.ld_flags
            # rpath flags to ensure the built shared object can find Boost at runtime
            boost_libdir = self.spec["boost"].prefix.lib
            rpath_flags = f"-Wl,-rpath,{boost_libdir}"
            boost_lib64dir = getattr(self.spec["boost"].prefix, "lib64", None)
            if boost_lib64dir and os.path.isdir(boost_lib64dir):
                rpath_flags += f" -Wl,-rpath,{boost_lib64dir}"
            # Prevent the linker from dropping Boost libs referenced from static cytolib
            no_as_needed = "-Wl,--no-as-needed"
            env.append_flags("LDFLAGS", boost_ldflags)
            env.append_flags("LDFLAGS", rpath_flags)
            env.append_flags("LDFLAGS", no_as_needed)
            env.append_flags("PKG_LIBS", boost_ldflags)
            env.append_flags("PKG_LIBS", rpath_flags)
            env.append_flags("PKG_LIBS", no_as_needed)
            # Ensure runtime finds the Spack Boost libs (avoid picking system Boost)
            boost_lib = self.spec["boost"].prefix.lib
            env.prepend_path("LD_LIBRARY_PATH", boost_lib)
            # Some platforms install to lib64
            boost_lib64 = getattr(self.spec["boost"].prefix, "lib64", None)
            if boost_lib64 and os.path.isdir(boost_lib64):
                env.prepend_path("LD_LIBRARY_PATH", boost_lib64)

    def patch(self):
        # Ensure Boost libs are added to PKG_LIBS during linking
        # because we link against static cytolib which depends on Boost.
        import os
        makevars_paths = [
            os.path.join("src", "Makevars"),
            os.path.join("src", "Makevars.in"),
        ]
        boost_ldflags = self.spec["boost"].libs.ld_flags
        for mv in makevars_paths:
            if os.path.exists(mv):
                with open(mv, "a", encoding="utf-8") as f:
                    # Link with Boost and embed rpath to Spack's Boost
                    f.write("\nPKG_LIBS += {}\n".format(boost_ldflags))
                    boost_libdir = self.spec["boost"].prefix.lib
                    f.write("PKG_LIBS += -Wl,-rpath,{}\n".format(boost_libdir))
                    boost_lib64dir = getattr(self.spec["boost"].prefix, "lib64", None)
                    if boost_lib64dir and os.path.isdir(boost_lib64dir):
                        f.write("PKG_LIBS += -Wl,-rpath,{}\n".format(boost_lib64dir))
                    # Ensure Boost libs are not dropped by --as-needed
                    f.write("PKG_LIBS += -Wl,--no-as-needed\n")
                break
