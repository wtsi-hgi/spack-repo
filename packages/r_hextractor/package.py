# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHextractor(RPackage):
	"""Integrated Tool for Hairping Extraction of RNA Sequences

	Simple and integrated tool that automatically extracts and folds all hairpin sequences from raw genome-wide data. It predicts the secondary structure of several overlapped segments, with longer length than the mean length of sequences of interest for the species under processing, ensuring that no one is lost nor inappropriately cut.
	"""
	
	cran = "HextractoR" 

	version("1.4", md5="9faa63580f5f592980181c31149794fe")

	depends_on("r-seqinr", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
