# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGivitir(RPackage):
	"""The GiViTI Calibration Test and Belt

	Functions to assess the calibration of logistic regression models with the GiViTI (Gruppo Italiano per la Valutazione degli interventi in Terapia Intensiva, Italian Group for the Evaluation of the Interventions in Intensive Care Units - see <http://www.giviti.marionegri.it/>) approach. The approach consists in a graphical tool, namely the GiViTI calibration belt, and in the associated statistical test. These tools can be used both to evaluate the internal calibration (i.e. the goodness of fit) and to assess the validity of an externally developed model.
	"""
	
	cran = "givitiR" 

	version("1.3", md5="fac6fdb0bcba4e1b408e2706c825bef8")

	depends_on("r-alabama", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
