# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFunmediation(RPackage):
	"""Functional Mediation for a Distal Outcome

	Fits a functional mediation model with a scalar distal outcome. The method is described in detail by Coffman, Dziak, Litson, Chakraborti, Piper & Li (2021) <arXiv:2112.03960>. The model is similar to that of Lindquist (2012) <doi:10.1080/01621459.2012.695640> although allowing a binary outcome as an alternative to a numerical outcome.  The current version is a minor bug fix in the vignette. The development of this package was part of a research project supported by National Institutes of Health grants P50 DA039838 from the National Institute of Drug Abuse and 1R01 CA229542-01 from the National Cancer Institute and the NIH Office of Behavioral and Social Science Research. Content is solely the responsibility of the authors and does not necessarily represent the official views of the funding institutions mentioned above. This software is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
	"""
	
	cran = "funmediation" 

	version("1.0.2", md5="7f956380239103ac0a93574dded90d3b")

	depends_on("r-refund", type=("build", "run"))
	depends_on("r-tvem", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
