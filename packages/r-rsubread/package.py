# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsubread(RPackage):
	"""Mapping, quantification and variant analysis of sequencing data

	Alignment, quantification and analysis of RNA sequencing data (including both bulk RNA-seq and scRNA-seq) and DNA sequenicng data (including ATAC-seq, ChIP-seq, WGS, WES etc). Includes functionality for read mapping, read counting, SNP calling, structural variant detection and gene fusion discovery. Can be applied to all major sequencing techologies and to both short and long sequence reads.
	"""
	
	homepage = "http://bioconductor.org/packages/Rsubread"
	bioc = "Rsubread" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Rsubread_2.16.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/Rsubread/Rsubread_2.16.1.tar.gz"]

	version("2.16.1", md5="ec5687eb02901ff3b62915cf37aa48b4")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("zlib", type=("build", "link", "run"))
