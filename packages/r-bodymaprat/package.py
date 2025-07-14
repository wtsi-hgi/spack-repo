# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBodymaprat(RPackage):
	"""Experimental dataset from the rat BodyMap project

	This package contains a SummarizedExperiment from the Yu et al. (2013) paper that performed the rat BodyMap across 11 organs and 4 developmental stages. Raw FASTQ files were downloaded and mapped using STAR. Data is available on ExperimentHub as a data package.
	"""
	
	bioc = "bodymapRat" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/bodymapRat_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/bodymapRat/bodymapRat_1.18.0.tar.gz"]

    version("1.24.0", tag="RELEASE_3_21")
	version("1.18.0", sha256="068ece05619032c39273622f90904a98cc51a21bf5da850b06149935fb36d8e9")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))

