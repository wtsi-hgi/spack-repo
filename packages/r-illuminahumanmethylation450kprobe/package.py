# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIlluminahumanmethylation450kprobe(RPackage):
	"""Probe sequence data for microarrays of type IlluminaHumanMethylation450k

	Probe sequences from Illumina (ftp.illumina.com) for hm450 probes
	"""
	
	bioc = "IlluminaHumanMethylation450kprobe" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/IlluminaHumanMethylation450kprobe_2.0.6.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/IlluminaHumanMethylation450kprobe/IlluminaHumanMethylation450kprobe_2.0.6.tar.gz"]

	version("2.0.6", sha256="2a46c84d45a416422bd4a95dfc40007ea6612923545863377f1ba376780650c5")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-annotationdbi@1.13.18:", type=("build", "run"))

