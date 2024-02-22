# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REra(RPackage):
	"""Year-Based Time Scales

	Provides a consistent representation of year-based time scales as a
    numeric vector with an associated 'era'. There are built-in era definitions
    for many year numbering systems used in contemporary and historic calendars 
    (e.g. Common Era, Islamic 'Hijri' years); year-based time scales used in 
    archaeology, astronomy, geology, and other palaeosciences (e.g. 
    Before Present, SI-prefixed 'annus'); and support for arbitrary user-defined
    eras. Years can converted from any one era to another using a generalised 
    transformation function. Methods are also provided for robust casting and 
    coercion between years and other numeric types, type-stable arithmetic with 
    years, and pretty-printing in tables.
	"""
	
	homepage = "https://era.joeroe.io"
	cran = "era" 

	version("0.4.1", md5="516d64fdd05f2e6a70fa1727fd5d400b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-vctrs@0.3:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-pillar", type=("build", "run"))
