# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMeme(RPackage):
	"""Create Meme

	The word 'Meme' was originated from the book, 'The Selfish Gene', authored by Richard Dawkins (1976).
             It is a unit of culture that is passed from one generation to another and correlates to the gene, the unit of physical heredity.
             The internet memes are captioned photos that are intended to be funny, ridiculous.
             Memes behave like infectious viruses and travel from person to person quickly through social media.
             The 'meme' package allows users to make custom memes.
	"""
	
	homepage = "https://github.com/GuangchuangYu/meme/"
	cran = "meme" 

	version("0.2.3", md5="6aeca8537a1184697d1c6935af8a41ad")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridgraphics", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
	depends_on("r-showtext", type=("build", "run"))
	depends_on("r-sysfonts", type=("build", "run"))
