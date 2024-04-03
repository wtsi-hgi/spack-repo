# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcmdrpluginEzr(RPackage):
	"""R Commander Plug-in for the EZR (Easy R) Package

	EZR (Easy R) adds a variety of statistical functions, including survival analyses, ROC analyses, metaanalyses, sample size calculation, and so on, to the R commander. EZR enables point-and-click easy access to statistical functions, especially for medical statistics. EZR is platform-independent and runs on Windows, Mac OS X, and UNIX. Its complete manual is available only in Japanese (Chugai Igakusha, ISBN: 978-4-498-10918-6, Nankodo, ISBN: 978-4-524-26158-1, Ohmsha, ISBN: 978-4-274-22632-8), but an report that introduced the investigation of EZR was published in Bone Marrow Transplantation (Nature Publishing Group) as an Open article. This report can be used as a simple manual. It can be freely downloaded from the journal website as shown below. This report has been cited in more than 10,000 scientific articles.
	"""
	
	homepage = "https://www.nature.com/articles/bmt2012244.pdf"
	cran = "RcmdrPlugin.EZR" 

	version("1.65", md5="c635167a27ec8c89351661f4bcb24984")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-rcmdr@2.8:", type=("build", "run"))
	depends_on("r-readstata13", type=("build", "run"))
