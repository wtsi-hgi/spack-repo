# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUnrtf(RPackage):
	"""Extract Text from Rich Text Format (RTF) Documents

	Wraps the 'unrtf' utility <https://www.gnu.org/software/unrtf/> to 
    extract text from RTF files. Supports document conversion to HTML, LaTeX or
    plain text. Output in HTML is recommended because 'unrtf' has limited 
    support for converting between character encodings.
	"""
	
	homepage = "https://docs.ropensci.org/unrtf/"
	cran = "unrtf" 

	version("1.4.5", md5="b9440c7ebde3e4cd10e30ba52589d179")

	depends_on("r-sys@2:", type=("build", "run"))
