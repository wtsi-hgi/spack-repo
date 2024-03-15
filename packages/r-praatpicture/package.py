# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPraatpicture(RPackage):
	"""'Praat Picture' Style Plots of Acoustic Data

	Quickly and easily generate plots of acoustic data aligned with transcriptions similar to those made in 'Praat' using either derived signals generated directly in R with 'wrassp' or imported derived signals from 'Praat'. Provides easy and fast out-of-the-box solutions but also a high extent of  flexibility. Also provides options for embedding audio in figures and animating figures.
	"""
	
	homepage = "https://github.com/rpuggaardrode/praatpicture"
	cran = "praatpicture" 

	version("1.0.0", md5="206457e6bdef98223c41e5859dcf65c8")

	depends_on("r-av@0.9:", type=("build", "run"))
	depends_on("r-crayon@1.5.2:", type=("build", "run"))
	depends_on("r-emur@2.4.2:", type=("build", "run"))
	depends_on("r-gifski@1.12.0.2:", type=("build", "run"))
	depends_on("r-gsignal@0.3.5:", type=("build", "run"))
	depends_on("r-ipa@0.1:", type=("build", "run"))
	depends_on("r-phontools@0.2.2.2:", type=("build", "run"))
	depends_on("r-rpraat@1.3.2.1:", type=("build", "run"))
	depends_on("r-rstudioapi@0.15:", type=("build", "run"))
	depends_on("r-soundgen@2.6.2:", type=("build", "run"))
	depends_on("r-tuner@1.4.6:", type=("build", "run"))
	depends_on("r-wrassp@1.0.4:", type=("build", "run"))
