# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGluedown(RPackage):
	"""Wrap Vectors in Markdown Formatting

	Ease the transition between R vectors and markdown
    text. With 'gluedown' and 'rmarkdown', users can create traditional
    vectors in R, glue those strings together with the markdown syntax,
    and print those formatted vectors directly to the document. This
    package primarily uses GitHub Flavored Markdown (GFM), an offshoot of
    the unambiguous CommonMark specification by John MacFarlane (2019)
    <https://spec.commonmark.org/>.
	"""
	
	homepage = "https://kiernann.github.io/gluedown/"
	cran = "gluedown" 

	version("1.0.8", md5="236b203ada0c500f7cfe6823d8ef419f")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-glue@1.3.1:", type=("build", "run"))
	depends_on("r-magrittr@2.0.1:", type=("build", "run"))
