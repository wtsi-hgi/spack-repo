# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZebrafishrnaseq(RPackage):
	"""Zebrafish RNA-Seq Experimental Data from Ferreira et al. (2014)

	Gene-level read counts from RNA-Seq for gallein-treated and control zebrafish.
	"""
	
	bioc = "zebrafishRNASeq" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/zebrafishRNASeq_1.22.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/zebrafishRNASeq/zebrafishRNASeq_1.22.0.tar.gz"]

	version("1.22.0", md5="c1fcbadec1b25e4b28483c015f7ab35c")

	depends_on("r@2.10:", type=("build", "run"))

	# experiment