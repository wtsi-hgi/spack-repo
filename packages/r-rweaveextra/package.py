# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRweaveextra(RPackage):
	"""Sweave Drivers with Extra Tricks Up their Sleeve

	Weave and tangle drivers for Sweave extending the
  standard drivers. RweaveExtraLatex and RtangleExtra provide options
  to completely ignore code chunks on weaving, tangling, or both.
  Chunks ignored on weaving are not parsed, yet are written out
  verbatim on tangling. Chunks ignored on tangling may be evaluated as
  usual on weaving, but are completely left out of the tangled
  scripts. The driver RtangleExtra also provides an option to specify
  the extension of the file name (or remove it entirely) when
  splitting is selected on tangling.
	"""
	
	homepage = "https://gitlab.com/vigou3/rweaveextra"
	cran = "RweaveExtra" 

	version("1.1-0", md5="1126c86deef9389769c5ab276f273735")

	depends_on("r@4.1.0:", type=("build", "run"))
