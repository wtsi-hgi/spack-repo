# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTelp(RPackage):
	"""Social Representation Theory Application: The Free Evocation of
Words Technique

	Using The Free Evocation of Words Technique method with some functions, this package will make a
    social representation and other analysis. The Free Evocation of Words Technique consists of collecting a number of words evoked by a subject facing exposure to an inducer term. The purpose of this technique is to understand the relationships created between words evoked by the individual and the inducer term. This technique is included in the theory of social representations, therefore, on the information transmitted by an individual, seeks to create a profile that define a social group.
	"""
	
	cran = "TELP" 

	version("1.0.2", md5="e72d832b0237f7eb8ce597fd86b8bcd5")

	depends_on("r-tcltk2", type=("build", "run"))
	depends_on("r-tm", type=("build", "run"))
	depends_on("r-wordcloud", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-arules", type=("build", "run"))
	depends_on("r-arulesviz", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
