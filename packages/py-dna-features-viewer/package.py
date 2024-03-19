# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyDnaFeaturesViewer(PythonPackage):
    """DNA Features Viewer is a Python library to visualize DNA features"""

    homepage = "https://github.com/Edinburgh-Genome-Foundry/DnaFeaturesViewer"
    pypi = "dna_features_viewer/dna_features_viewer-3.1.3.tar.gz"

    version("3.1.3", sha256="7af179ab1b3c0dedd09e9e667cbd0fb804721ecbfc0cb4d0dda8a165437b3919")
    version("3.1.2", sha256="b8b2b7657e2a9f165edd6f68fb679abfa0c2fdeb887cbd04c22b514997f52d12")

    depends_on("python@3.9.9", type=("build", "run"))

    depends_on("py-matplotlib@3.0.0:", type=("build", "run"))
    depends_on("py-biopython", type=("build", "run"))
    depends_on("py-packaging", type=("build", "run"))

    depends_on("py-setuptools", type="build")

