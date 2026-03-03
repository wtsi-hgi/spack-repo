# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyHicexplorer(PythonPackage):
    """Set of programs to process, analyze and visualize Hi-C data"""

    homepage = "http://hicexplorer.readthedocs.io"

    url = "https://github.com/deeptools/HiCExplorer/archive/refs/tags/3.7.5.tar.gz"

    version("3.7.5", sha256="5d798d47bc4b4067e9a1446a5745c8146e073b7d9df18390eb1f414a741d2715")

    depends_on("py-configparser", type=("build", "run"))
    depends_on("py-hic2cool", type=("build", "run"))
    depends_on("py-psutil", type=("build", "run"))
    depends_on("py-pygenometracks", type=("build", "run"))
    depends_on("py-hicmatrix", type=("build", "run"))
    depends_on("py-unidecode", type=("build", "run"))
    depends_on("py-jinja2", type=("build", "run"))
    depends_on("py-cooler", type=("build", "run"))
    depends_on("py-future", type=("build", "run"))
    depends_on("py-six", type=("build", "run"))
    depends_on("py-pybigwig", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-tables", type=("build", "run"))
    depends_on("py-biopython", type=("build", "run"))
    depends_on("py-intervaltree", type=("build", "run"))
    depends_on("py-pysam", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-krbalancing@0.0.5:", type=("build", "run"))
    depends_on("py-scikit-learn@1.3:1.4", type=("build", "run"))
    depends_on("py-imbalanced-learn@0.11:", type=("build", "run"))
    depends_on("py-fit-nbinom@1.2:", type=("build", "run"))
    depends_on("py-graphviz@0.20:", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-cleanlab@2.5:", type=("build", "run"))
