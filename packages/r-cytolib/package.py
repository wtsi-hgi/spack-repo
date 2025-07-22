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
    depends_on("boost@1.72.0:+filesystem+system", type=("build", "link", "run"))

    def patch(self):
        bundled_boost_dir = "src/boost"
        if os.path.exists(bundled_boost_dir):
            shutil.rmtree(bundled_boost_dir)
