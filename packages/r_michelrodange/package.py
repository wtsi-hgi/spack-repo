# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMichelrodange(RPackage):
	"""The Works (in Luxembourguish) of Michel Rodange

	Michel Rodange was a Luxembourguish writer and poet who lived in the 19th century. 
    His most notable work is Rodange (1872, ISBN:1166177424), ("Renert oder de Fuuß am Frack an a Ma'nsgrëßt"),
    but he also wrote many more works, including Rodange, Tockert (1928) <https://www.autorenlexikon.lu/page/document/361/3614/1/FRE/index.html> 
    ("D'Léierchen - Dem Léiweckerche säi Lidd") and Rodange, Welter (1929) <https://www.autorenlexikon.lu/page/document/361/3615/1/FRE/index.html>
    ("Dem Grow Sigfrid seng Goldkuommer"). This package contains three datasets, each made from the
    plain text versions of his works available on 
    <https://data.public.lu/fr/datasets/the-works-in-luxembourguish-of-michel-rodange/>.
	"""
	
	homepage = "https://github.com/b-rodrigues/michelRodange"
	cran = "michelRodange" 

	version("1.0.0", md5="da0f325c50faf673894dea159b15af51")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
