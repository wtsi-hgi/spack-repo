# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
import os
import shutil

class RCytolib(RPackage):
    """C++ infrastructure for representing and interacting with the gated cytometry data

    This package provides the core data structure and API to represent and interact with the gated cytometry data.
    """

    bioc = "cytolib"

    version("2.20.0", commit="262eb4a0cba2ec58795468963f0f948b97662788")
    version("2.14.1", commit="4e456ea7bc236eefd6c5f48f33f64729c8c08857")

    depends_on("r@3.4:", type=("build", "run"))
    depends_on("r-rprotobuflib@2.13.1:", type=("build", "run"))
    depends_on("r-bh@1.84:", type=("build", "run"))
    depends_on("r-rhdf5lib", type=("build", "run"))
    # Align Boost with BH headers and flowCore to prevent ABI/link issues
    depends_on("boost@1.84:+filesystem+system cxxstd=17", type=("build", "link", "run"))

    def setup_build_environment(self, env):
        # Force cytolib to link against the Spack-provided Boost libraries
        # and avoid autodetected system Boost with legacy -mt suffix.
        boost = self.spec["boost"]
        env.set("BOOST_CPPFLAGS", f"-I{boost.prefix.include}")
        env.set("BOOST_LDFLAGS", boost.libs.ld_flags)
        env.set("BOOST_LIBS", boost.libs.ld_flags)
        # Help the dynamic loader find Spack Boost at runtime
        env.prepend_path("LD_LIBRARY_PATH", boost.prefix.lib)
        lib64 = getattr(boost.prefix, "lib64", None)
        if lib64 and os.path.isdir(lib64):
            env.prepend_path("LD_LIBRARY_PATH", lib64)

    def patch(self):
        bundled_boost_dir = "src/boost"
        if os.path.exists(bundled_boost_dir):
            shutil.rmtree(bundled_boost_dir)
