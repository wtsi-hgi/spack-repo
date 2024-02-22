# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLexfindr(RPackage):
	"""Find Related Items and Lexical Dimensions in a Lexicon

	Implements code to identify lexical competitors in a given list
  of words. We include many of the standard competitor types used in spoken word
  recognition research, such as functions to find cohorts, neighbors, and
  rhymes, amongst many others. The package includes documentation for using a
  variety of lexicon files, including those with form codes made up of multiple
  letters (i.e., phoneme codes) and also basic orthographies. Importantly, the
  code makes use of multiple CPU cores and vectorization when possible, making
  it extremely fast and able to handle large lexicons. Additionally, the package
  contains documentation for users to easily write new functions, allowing
  researchers to examine other relationships within a lexicon. 
  Preprint: <https://psyarxiv.com/8dyru/>. Open access: <https://link.springer.com/epdf/10.3758/s13428-021-01667-6?sharing_token=9WlO9soCc9y0uSuwWSUYfJAH0g46feNdnc402WrhzyrdKcK8uzZx_hDEtgbYzn3gvxdG5Cuj0j0cC4lVMFBqYCGTQmE2blN2Gwo74LJ8ro1pEOAYDRFy6Lhf1nc719vD-zU7GDvKOQxDAwPbrisvPBeXSIu0NkqXF7Jx3IuUwIs%3D>. 
  Citation: Li, Z., Crinnion, A.M. & Magnuson, J.S. (2021). 
  <doi:10.3758/s13428-021-01667-6>.
	"""
	
	homepage = "https://github.com/maglab-uconn/LexFindR"
	cran = "LexFindR" 

	version("1.0.2", md5="7bc4bfb05849ccf76874e6e102fbec87")

	depends_on("r@3.5:", type=("build", "run"))
