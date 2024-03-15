# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNanotubes(RPackage):
	"""Mouse nanotube CAGE data

	Cap Analysis of Gene Expression (CAGE) data from "Identification of Gene Transcription Start Sites and Enhancers Responding to Pulmonary Carbon Nanotube Exposure in Vivo" by Bornholdt et al. supplied as CAGE Transcription Start Sites (CTSSs).
	"""
	
	homepage = "https://github.com/MalteThodberg/nanotubes"
	bioc = "nanotubes" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/nanotubes_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/nanotubes/nanotubes_1.18.0.tar.gz"]

	version("1.18.0", md5="ff283cb49c319a357c22e17d2df22715")

	depends_on("r@3.6:", type=("build", "run"))

	# experiment