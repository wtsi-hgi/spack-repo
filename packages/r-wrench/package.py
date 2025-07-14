# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWrench(RPackage):
	"""Wrench normalization for sparse count data

	Wrench is a package for normalization sparse genomic count data, like that arising from 16s metagenomic surveys.
	"""
	
	homepage = "https://github.com/HCBravoLab/Wrench"
	bioc = "Wrench" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Wrench_1.20.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/Wrench/Wrench_1.20.0.tar.gz"]

    version("1.26.0", tag="RELEASE_3_21")
	version("1.20.0", sha256="2dcdf1f0d1ebe8feeeaf4aec752c22f744b3e1f28c697d527094c2128650e685")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-locfit", type=("build", "run"))
