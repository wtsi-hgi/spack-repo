# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGeosketch(PythonPackage):
    """geosketch is a Python package that implements the geometric sketching algorithm described by Brian Hie, Hyunghoon Cho, Benjamin DeMeo, Bryan Bryson, and Bonnie Berger in "Geometric sketching compactly summarizes the single-cell transcriptomic landscape", Cell Systems (2019)."""

    homepage = "https://github.com/brianhie/geosketch"
    pypi = "geosketch/geosketch-1.2.tar.gz"

    version("1.2", sha256="bbfe97366b91c5927b6076d5a6738d9cfbe094efb5ac1117aab7a30b6081cc4e")

    depends_on("py-fbpca@1.0:", type=("build", "run"))
    depends_on("py-numpy@1.12.0:", type=("build", "run"))
    depends_on("py-scikit-learn@0.24:", type=("build", "run"))
