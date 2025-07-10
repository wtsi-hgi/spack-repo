# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnota(RPackage):
	"""ANalysis Of Translational Activity (ANOTA).

	Genome wide studies of translational control is emerging as a tool to study verious biological conditions. The output from such analysis is both the mRNA level (e.g. cytosolic mRNA level) and the levl of mRNA actively involved in translation (the actively translating mRNA level) for each mRNA. The standard analysis of such data strives towards identifying differential translational between two or more sample classes - i.e. differences in actively translated mRNA levels that are independent of underlying differences in cytosolic mRNA levels. This package allows for such analysis using partial variances and the random variance model. As 10s of thousands of mRNAs are analyzed in parallell the library performs a number of tests to assure that the data set is suitable for such analysis.
	"""
	
	bioc = "anota" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/anota_1.50.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/anota/anota_1.50.0.tar.gz"]

	version("1.50.0", sha256="6151694aa3a54cc96f41ddd2803caa96230f3dd30ae7c15d4274731ab93c39ac")

	depends_on("r-qvalue", type=("build", "run"))
	depends_on("r-multtest", type=("build", "run"))
