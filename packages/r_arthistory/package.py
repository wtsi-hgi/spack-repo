# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArthistory(RPackage):
	"""Art History Textbook Data

	Data from Gardner and Janson art history textbooks about both the artists featured in these books as well as their works.
    See Helen Gardner ("Art through the ages; an introduction to its history and significance," 1926, <https://find.library.duke.edu/catalog/DUKE000104481>.
    Helen Gardner, revised by Horst de la Croix and Richard G. Tansey ("Gardner’s Art through the ages," 1980, ISBN: 0155037587).
    Fred S. Kleiner ("Gardner’s art through the ages: a global history," 2020, ISBN: 9781337630702).
    Horst de la Croix and Richard G. Tansey ("Gardner's art through the ages," 1986, ISBN: 0155037633).
    Helen Gardner ("Art through the ages; an introduction to its history and significance," 1936, <https://find.library.duke.edu/catalog/DUKE001199463>).
    Helen Gardner ("Art through the ages," 1948, <https://find.library.duke.edu/catalog/DUKE001199466>).
    Helen Gardner, revised under the editorship of Sumner M. Crosby ("Art through the ages," 1959, <https://find.library.duke.edu/catalog/DUKE001199469>).
    Helen Gardner, revised by Horst de la Croix and Richard G. Tansey ("Gardner’s Art through the ages," 1975, ISBN: 0155037560).
    Fred S. Kleiner ("Gardner’s Art through the ages: a global history," 2013, ISBN: 9780495915423.
    Fred S. Kleiner, Christin J. Mamiya, Richard G. Tansey ("Gardner’s art through the ages," 2001, ISBN: 0155083155).
    Fred S. Kleiner ("Gardner’s Art through the ages: a global history," 2016, ISBN: 9781285837840).
    Fred S. Kleiner, Christin J. Mamiya ("Gardner’s art through the ages," 2005, ISBN: 0534640958).
    Helen Gardner, revised by Horst de la Croix and Richard G. Tansey ("Gardner’s Art through the ages," 1970, ISBN: 0155037528).
    Helen Gardner, Richard G. Tansey, Fred S. Kleiner ("Gardner’s Art through the ages," 1996, ISBN: 0155011413).
    Helen Gardner, Horst de la Croix, Richard G. Tansey, Diane Kirkpatrick ("Gardner’s Art through the ages," 1991, ISBN: 0155037692).
    Helen Gardner, Fred S. Kleiner ("Gardner’s Art through the ages: a global history," 2009, ISBN: 9780495093077).
    Davies, Penelope J.E., Walter B. Denny, Frima Fox Hofrichter, Joseph F. Jacobs, Ann S. Roberts, David L. Simon ("Janson’s history of art: the western tradition," 2007, ISBN: 0131934554).
    Davies, Penelope J.E., Walter B. Denny, Frima Fox Hofrichter, Joseph F. Jacobs, Ann S. Roberts, David L. Simon ("Janson’s history of art: the western tradition," 2011, ISBN: 9780205685172).
    H. W. Janson, Anthony F. Janson ("History of Art," 2001, ISBN: 0810934469).
    H. W. Janson, revised and expanded by Anthony F. Janson ("History of art," 1986, ISBN: 013389388).
    H. W. Janson, Dora Jane Janson ("History of art: a survey of the major visual arts from the dawn of history to present day," 1977, ISBN: 0810910527).
    H. W. Janson, Dora Jane Janson ("History of art: a survey of the major visual arts from the dawn of history to present day," 1969, <https://find.library.duke.edu/catalog/DUKE000005734>).
    H. W. Janson, Dora Jane Janson ("History of art: a survey of the major visual arts from the dawn of history to present day," 1963, <https://find.library.duke.edu/catalog/DUKE001521852>).
    H. W. Janson, revised and expanded by Anthony F. Janson ("History of art," 1991, ISBN: 0810934019).
    H. W. Janson, revised and expanded by Anthony F. Janson ("History of art," 1995, ISBN: 0810934213).
	"""
	
	homepage = "https://github.com/saralemus7/arthistory"
	cran = "arthistory" 

	version("0.1.0", md5="550334a6ba8ae74fc7d43ed8078fe3f9")

	depends_on("r@2.10:", type=("build", "run"))
