# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMidastouch(RPackage):
	"""Multiple Imputation by Distance Aided Donor Selection

	Contains the function mice.impute.midastouch(). Technically this function is to be run from within the 'mice' package (van Buuren et al. 2011), type ??mice. It substitutes the method 'pmm' within mice by 'midastouch'. The authors have shown that 'midastouch' is superior to default 'pmm'. Many ideas are based on Siddique / Belin 2008's  MIDAS.
	"""
	
	homepage = "https://www.uni-bamberg.de/fileadmin/uni/fakultaeten/sowi_lehrstuehle/statistik/Personen/Dateien_Florian/properPMM.pdf"
	cran = "midastouch" 

	version("1.3", md5="132eaa2ee398ff6d11b62df885b919a6")

	depends_on("r@3.2:", type=("build", "run"))
