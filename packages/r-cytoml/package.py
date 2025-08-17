# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
import os


class RCytoml(RPackage):
    """A GatingML Interface for Cross Platform Cytometry Data Sharing

    Uses platform-specific implemenations of the GatingML2.0 standard to exchange gated cytometry data with other software platforms.
    """

    homepage = "https://github.com/RGLab/CytoML"
    bioc = "CytoML"

    version("2.20.0", commit="f8765f5131abf4f80057c27c232396726f7b1b0c")
    version("2.14.0", commit="47100567ec21fd53b5f5752e629432478eb32729")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-cytolib", type=("build", "run"))
    depends_on("r-flowcore@1.99.10:", type=("build", "run"))
    depends_on("r-flowworkspace", type=("build", "run"))
    depends_on("r-opencyto@1.99.2:", type=("build", "run"))
    depends_on("r-xml", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-jsonlite", type=("build", "run"))
    depends_on("r-rbgl", type=("build", "run"))
    depends_on("r-rgraphviz", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-graph", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-ggcyto@1.11.4:", type=("build", "run"))
    depends_on("r-yaml", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-cpp11", type=("build", "run"))
    depends_on("r-bh@1.62.0.1:", type=("build", "run"))
    depends_on("r-rprotobuflib", type=("build", "run"))
    depends_on("r-rhdf5lib", type=("build", "run"))
    depends_on("libxml2", type=("build", "link", "run"))
    # CytoML uses Boost filesystem via BH headers; ensure we link against
    # Spack Boost libraries to satisfy symbols at load time and align with
    # RCytolib's Boost settings to avoid ABI mismatches.
    depends_on("boost@1.84:+filesystem+system cxxstd=17", type=("build", "link", "run"))

    def setup_build_environment(self, env):
        boost = self.spec["boost"]
        # Help the package discover and link the Spack-provided Boost
        env.set("BOOST_CPPFLAGS", f"-I{boost.prefix.include}")
        env.set("BOOST_LDFLAGS", boost.libs.ld_flags)
        env.set("BOOST_LIBS", boost.libs.ld_flags)
        # Ensure configure's @PKG_LIBS@ includes Boost by populating
        # CYTOLIBML_LIBS which is concatenated into PKG_LIBS in configure.ac
        env.append_flags("CYTOLIBML_LIBS", boost.libs.ld_flags)
        # Make runtime linker find Boost
        env.prepend_path("LD_LIBRARY_PATH", boost.prefix.lib)
        lib64 = getattr(boost.prefix, "lib64", None)
        if lib64 and os.path.isdir(lib64):
            env.prepend_path("LD_LIBRARY_PATH", lib64)
