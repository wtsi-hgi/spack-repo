# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFbpca(PythonPackage):
    """Functions for principal component analysis (PCA)."""

    homepage = "https://github.com/facebookarchive/fbpca"
    pypi = "fbpca/fbpca-1.0.tar.gz"

    version("1.0", sha256="150677642479663f317fdbb5e06dab3f98721cf7031bb4a84113d7a631c472d1")

    depends_on("py-numpy@1.9:", type=("build", "run"))
    depends_on("py-scipy@0.14:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
