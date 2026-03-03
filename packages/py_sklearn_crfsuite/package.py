# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySklearnCrfsuite(PythonPackage):
    """sklearn-crfsuite is a thin CRFsuite (python-crfsuite) wrapper which provides interface simlar to scikit-learn. """

    homepage = "https://github.com/TeamHG-Memex/sklearn-crfsuite"
    pypi = "sklearn-crfsuite/sklearn-crfsuite-0.3.6.tar.gz"

    version("0.3.6", sha256="2f59aad3055e01a778a79a6352891cac04788e8b52688aa5bc8b11be7717861e")

    depends_on("py-tqdm@2.0:", type=("build", "run"))
    depends_on("py-tabulate@0.7.5:", type=("build", "run"))
    depends_on("py-scikit-learn@0.15:", type=("build", "run"))
    depends_on("py-python-crfsuite@0.8.3:", type=("build", "run"))
