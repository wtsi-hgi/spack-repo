# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyScanorama(PythonPackage):
    """Scanorama enables batch-correction and integration of heterogeneous scRNA-seq datasets."""

    homepage = "https://github.com/brianhie/scanorama"
    pypi = "scanorama/scanorama-1.7.4.tar.gz"

    version("1.7.4", sha256="67de100e63abc3028c7780d3a217e43e920a5781230bc6b6a51349d4605e005c")

    depends_on("py-annoy@1.11.5:", type=("build", "run"))
    depends_on("py-fbpca@1.0:", type=("build", "run"))
    depends_on("py-geosketch@1.0:", type=("build", "run"))
    depends_on("py-intervaltree@3.1.0:", type=("build", "run"))
    depends_on("py-matplotlib@2.0.2:", type=("build", "run"))
    depends_on("py-numpy@1.12.0:", type=("build", "run"))
    depends_on("py-scipy@1.0.0:", type=("build", "run"))
    depends_on("py-scikit-learn@0.20:", type=("build", "run"))
