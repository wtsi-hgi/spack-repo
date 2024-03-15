# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMassarray(RPackage):
	"""Analytical Tools for MassArray Data

	This package is designed for the import, quality control, analysis, and visualization of methylation data generated using Sequenom's MassArray platform.  The tools herein contain a highly detailed amplicon prediction for optimal assay design. Also included are quality control measures of data, such as primer dimer and bisulfite conversion efficiency estimation. Methylation data are calculated using the same algorithms contained in the EpiTyper software package.  Additionally, automatic SNP-detection can be used to flag potentially confounded data from specific CG sites.  Visualization includes barplots of methylation data as well as UCSC Genome Browser-compatible BED tracks.  Multiple assays can be positionally combined for integrated analysis.
	"""
	
	bioc = "MassArray" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MassArray_1.54.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MassArray/MassArray_1.54.0.tar.gz"]

	version("1.54.0", md5="028fea456ce2e5b3820ad6dc0d1989c1")

	depends_on("r@2.10:", type=("build", "run"))
