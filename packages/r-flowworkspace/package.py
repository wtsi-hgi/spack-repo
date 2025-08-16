# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
import os


class RFlowworkspace(RPackage):
    """Infrastructure for representing and interacting with gated and ungated cytometry data sets.

    This package is designed to facilitate comparison of automated gating methods against manual gating done in flowJo. This package allows you to import basic flowJo workspaces into BioConductor and replicate the gating from flowJo using the flowCore functionality. Gating hierarchies, groups of samples, compensation, and transformation are performed so that the output matches the flowJo analysis.
    """

    bioc = "flowWorkspace"

    version("4.20.0", commit="6963021e1e103806dc28557ccdec6f396b33d859")
    version("4.14.3", commit="7447e9ee630374f0878879532354892b72b3a093")
    version("4.14.2", md5="8c13b6aa80732d54f36bb544adba5a6c")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-cytolib@2.3.7:", type=("build", "run"))
    depends_on("r-xml", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-graph", type=("build", "run"))
    depends_on("r-rbgl", type=("build", "run"))
    depends_on("r-rgraphviz", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-scales@1.3:", type=("build", "run"))
    depends_on("r-matrixstats", type=("build", "run"))
    depends_on("r-rprotobuflib@1.99.4:", type=("build", "run"))
    depends_on("r-flowcore@2.1.1:", type=("build", "run"))
    depends_on("r-ncdfflow@2.25.4:", type=("build", "run"))
    depends_on("r-delayedarray", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-cpp11", type=("build", "run"))
    depends_on("r-bh@1.62.0.1:", type=("build", "run"))
    depends_on("r-rhdf5lib", type=("build", "run"))
    depends_on("zlib", type=("build", "link", "run"))

    # Ensure Boost libraries are available at link and runtime. Similar to
    # flowCore, flowWorkspace ends up requiring Boost symbols via cytolib and
    # friends; explicitly link Boost to avoid undefined symbols on load.
    depends_on("boost@1.84:+filesystem+system cxxstd=17", type=("link"))
    # Ensure LAPACK/BLAS symbols like dgelsd_ are resolved at link/load
    depends_on("blas", type=("link"))
    depends_on("lapack", type=("link"))

    def setup_build_environment(self, env):
        # Prefer Spack Boost headers/libs and ensure they are retained by the
        # linker (work around --as-needed) and are discoverable at runtime.
        if "boost" in self.spec:
            boost_inc = self.spec["boost"].prefix.include
            env.append_flags("CPPFLAGS", f"-I{boost_inc}")
            env.append_flags("CXXFLAGS", f"-I{boost_inc}")
            env.append_flags("PKG_CPPFLAGS", f"-I{boost_inc}")

            boost_ldflags = self.spec["boost"].libs.ld_flags
            boost_libdir = self.spec["boost"].prefix.lib
            rpath_flags = f"-Wl,-rpath,{boost_libdir}"
            boost_lib64dir = getattr(self.spec["boost"].prefix, "lib64", None)
            if boost_lib64dir and os.path.isdir(boost_lib64dir):
                rpath_flags += f" -Wl,-rpath,{boost_lib64dir}"

            # Compose link flags for Boost and BLAS/LAPACK
            blas_ldflags = self.spec["blas"].libs.ld_flags if "blas" in self.spec else ""
            lapack_ldflags = self.spec["lapack"].libs.ld_flags if "lapack" in self.spec else ""
            pkglibs_prefix = f"-Wl,--no-as-needed {boost_ldflags} {lapack_ldflags} {blas_ldflags} {rpath_flags}"
            env.append_flags("PKG_LIBS", pkglibs_prefix)
            env.append_flags("LDFLAGS", pkglibs_prefix)

            # Help runtime linker prefer Spack Boost
            env.prepend_path("LD_LIBRARY_PATH", boost_libdir)
            if boost_lib64dir and os.path.isdir(boost_lib64dir):
                env.prepend_path("LD_LIBRARY_PATH", boost_lib64dir)

    def patch(self):
        # If package provides src/Makevars, make sure Boost link flags are
        # injected and --no-as-needed is set so -lboost_* are kept.
        makevars_paths = [os.path.join("src", "Makevars"), os.path.join("src", "Makevars.in")]
        boost_ldflags = self.spec["boost"].libs.ld_flags if "boost" in self.spec else ""
        blas_ldflags = self.spec["blas"].libs.ld_flags if "blas" in self.spec else ""
        lapack_ldflags = self.spec["lapack"].libs.ld_flags if "lapack" in self.spec else ""
        for mv in makevars_paths:
            if os.path.exists(mv):
                with open(mv, "r", encoding="utf-8") as fh:
                    content = fh.read()
                lines = content.splitlines()
                new_lines = []
                inserted_prefix = False
                for line in lines:
                    new_lines.append(line)
                    if not inserted_prefix and line.strip().startswith("PKG_LIBS") and "=" in line:
                        new_lines.append("PKG_LIBS := -Wl,--no-as-needed $(PKG_LIBS)")
                        inserted_prefix = True
                boost_libdir = self.spec["boost"].prefix.lib if "boost" in self.spec else None
                if boost_ldflags:
                    new_lines.append(f"PKG_LIBS += {boost_ldflags}")
                if lapack_ldflags:
                    new_lines.append(f"PKG_LIBS += {lapack_ldflags}")
                if blas_ldflags:
                    new_lines.append(f"PKG_LIBS += {blas_ldflags}")
                if boost_libdir:
                    new_lines.append(f"PKG_LIBS += -Wl,-rpath,{boost_libdir}")
                    boost_lib64dir = getattr(self.spec["boost"].prefix, "lib64", None)
                    if boost_lib64dir and os.path.isdir(boost_lib64dir):
                        new_lines.append(f"PKG_LIBS += -Wl,-rpath,{boost_lib64dir}")
                # Normalize away -mt suffixed boost names if upstream hardcodes them
                new_lines.append("PKG_LIBS := $(patsubst -lboost_filesystem-mt,-lboost_filesystem,$(PKG_LIBS))")
                new_lines.append("PKG_LIBS := $(patsubst -lboost_system-mt,-lboost_system,$(PKG_LIBS))")
                with open(mv, "w", encoding="utf-8") as fh:
                    fh.write("\n".join(new_lines) + "\n")
                break
