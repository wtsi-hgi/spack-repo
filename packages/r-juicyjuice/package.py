# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJuicyjuice(RPackage):
	"""Inline CSS Properties into HTML Tags Using 'juice'

	There are occasions where you need a piece of HTML with integrated
    styles. A prime example of this is HTML email. This transformation
    involves moving the CSS and associated formatting instructions from the
    style block in the head of your document into the body of the HTML. Many
    prominent email clients require integrated styles in HTML email; otherwise a
    received HTML email will be displayed without any styling. This package will
    quickly and precisely perform these CSS transformations when given HTML text
    and it does so by using the JavaScript 'juice' library.
	"""
	
	homepage = "https://github.com/rich-iannone/juicyjuice"
	cran = "juicyjuice" 

	version("0.1.0", md5="bf3db84d36b3734e9c323eb0e9b0b4a3")

	depends_on("r-v8@4.2:", type=("build", "run"))
