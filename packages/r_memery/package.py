# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMemery(RPackage):
	"""Internet Memes for Data Analysts

	Generates internet memes that optionally include a superimposed inset plot and other atypical features, 
    combining the visual impact of an attention-grabbing meme with graphic results of data analysis.
    The package differs from related packages that focus on imitating and reproducing standard memes.
    Some packages do this by interfacing with online meme generators whereas others achieve this natively.
    This package takes the latter approach. It does not interface with online meme generators or require any authentication with external websites.
    It reads images directly from local files or via URL and meme generation is done by the package.
    While this is similar to the 'meme' package available on CRAN, it differs in that the focus is on 
    allowing for non-standard meme layouts and hybrids of memes mixed with graphs.
    While this package can be used to make basic memes like an online meme generator would produce, 
    it caters primarily to hybrid graph-meme plots where the meme presentation can be seen as a backdrop highlighting 
    foreground graphs of data analysis results.
    The package also provides support for an arbitrary number of meme text labels with arbitrary size, position and other attributes 
    rather than restricting to the standard top and/or bottom text placement. 
    This is useful for proper aesthetic interleaving of plots of data between meme image backgrounds and overlain text labels.
    The package offers a selection of templates for graph placement and appearance with respect to the underlying meme.
    Graph templates also permit additional template-specific customization.
    Animated gif support is provided but this is optional and functional only if the 'magick' package is installed. 
    'magick' is not required unless gif functionality is desired.
	"""
	
	homepage = "https://github.com/leonawicz/memery"
	cran = "memery" 

	version("0.5.7", md5="43794fe2d2fbdd86d7909581e388aa23")

	depends_on("r-showtext", type=("build", "run"))
	depends_on("r-sysfonts", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-jpeg", type=("build", "run"))
	depends_on("r-cairo", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
	depends_on("r-colourpicker", type=("build", "run"))
