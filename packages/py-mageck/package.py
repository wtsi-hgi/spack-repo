# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMageck(PythonPackage):
    """Model-based Analysis of Genome-wide CRISPR-Cas9 Knockout (MAGeCK) is a computational tool to identify important genes from the recent genome-scale CRISPR-Cas9 knockout screens (or GeCKO) technology. MAGeCK is developed by Wei Li and Han Xu from Dr. Xiaole Shirley Liu's lab at Dana-Farber Cancer Institute, and is being actively updated by Wei Li lab from Children's National Medical Center."""

    homepage = "https://sourceforge.net/p/mageck/wiki/Home/"
    url = "https://sourceforge.net/projects/mageck/files/0.5/mageck-0.5.9.5.tar.gz/download"

    version("0.5.9.5", sha256="b06a18036da63959cd7751911a46727aefe2fb1d8dd79d95043c3e3bdaf1d93a")

    depends_on("py-setuptools", type="build")

    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
