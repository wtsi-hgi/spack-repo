# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiathor(RPackage):
	"""Calculate Ecological Information and Diatom Based Indices

	
    Calculates ecological information and biotic indices for diatoms in a sample. 
    It includes number/shape of chloroplasts diversity indices, size classes, ecological guilds, and multiple biotic indices.
    It outputs both a dataframe with all the results and plots of all the obtained data in a defined output folder.
    Sample data was taken from Nicolosi Gelis, Cochero & Gómez (2020, <doi:10.1016/j.ecolind.2019.105951>).
    The package uses the 'Diat.Barcode' database to calculate morphological and ecological information by Rimet & Couchez (2012, <doi:10.1051/kmae/2012018>),
    and the combined classification of guilds and size classes established by B-Béres et al. (2017, <doi:10.1016/j.ecolind.2017.07.007>).
    Current diatom-based biotic indices include the DES index by Descy (1979, <https://pascal-francis.inist.fr/vibad/index.php?action=getRecordDetail&idt=PASCAL8060205402>), 
    the EPID index by Dell'Uomo (1996, ISBN: 3950009002), 
    the IDAP index by Prygiel & Coste (1993, <doi:10.1007/BF00028033>),
    the ID-CH index by Hürlimann & Niederhauser (2007, <https://www.bafu.admin.ch/bafu/fr/home/themes/eaux/publications/publications-eaux/methodes-analyse-appreciation-cours-eau-diatomees.html>),
    the IDP index by Gómez & Licursi (2001, <doi:10.1023/A:1011415209445>), 
    the ILM index by Leclercq & Maquet (1987, <https://www.vliz.be/imisdocs/publications/286641.pdf>),
    the IPS index by Coste (1982, <https://www.oieau.org/eaudoc/notice/ETUDE-DES-METHODES-BIOLOGIQUES-DAPPRECIATION-QUANTITATIVE-DE-LA-QUALITE-DES-EAUX>), 
    the LOBO index by Lobo, Callegaro, & Bender (2002, ISBN:9788585869908), 
    the SLA by Sládeček (1986, <doi:10.1002/aheh.19860140519>), 
    the TDI index by Kelly, & Whitton (1995, <doi:10.1007/BF00003802>), 
    the SPEAR(herbicide) index by Wood, Mitrovic, Lim, Warne, Dunlop, & Kefford (2019, <doi:10.1016/j.ecolind.2018.12.035>),
    the PBIDW index by Castro-Roa & Pinilla-Agudelo (2014), 
    and the DISP index by Stenger-Kovácsa et al. (2018).
	"""
	
	cran = "diathor" 

	version("0.1.0", md5="62e5090721c84bedfa224c6a205f31b1")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-stringdist", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
