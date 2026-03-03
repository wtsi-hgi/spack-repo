# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrosstabsLoglinear(RPackage):
	"""Cross Tabulation and Loglinear Analyses of Categorical Data

	Provides 'SPSS'- and 'SAS'-like output for cross tabulations of two
  categorical variables (CROSSTABS) and for hierarchical loglinear analyses 
  of two or more categorical variables (LOGLINEAR). The methods are described in
  Agresti (2013, ISBN:978-0-470-46363-5),
  Ajzen & Walker (2021, ISBN:9780429330308),
  Field (2018, ISBN:9781526440273),
  Norusis (2012, ISBN:978-0-321-74843-0),
  Nussbaum (2015, ISBN:978-1-84872-603-1),
  Stevens (2009, ISBN:978-0-8058-5903-4),
  Tabachnik & Fidell (2019, ISBN:9780134790541), and
  von Eye & Mun (2013, ISBN:978-1-118-14640-8).
	"""
	
	cran = "Crosstabs.Loglinear" 

	version("0.1.1", md5="556276fc772c5c089fdd19a805ae87e3")

