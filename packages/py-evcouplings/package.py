# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyEvcouplings(PythonPackage):
    """A Framework for evolutionary couplings analysis"""

    homepage = "https://github.com/debbiemarkslab/EVcouplings"
    pypi = "evcouplings/evcouplings-0.2.1-py2.py3-none-any.whl"

    version("0.0.1", sha256="c16eed4c0137be5a2c7406b9250fa1f292d2067fa79e24745c6052a599b9892a")
    version("0.0.2", sha256="c4a6d2c6e33a5e8b1d1b6b9987b8d673470ccf761295022e52a136bb97ff654a")
    version("0.0.3", sha256="92f9bd80a1b48900484782c8bee4d1e2969fc07f11907a14bcb54275714251be")
    version("0.0.4", sha256="3c4d69cca93fa42bbf975dbc4455d511601bd9748a87b98296fd13646bb86b70")
    version("0.0.5", sha256="08a8d3712076688c1b848537cdd711489b04da08f77725d496e1696126f15026")
    version("0.1.1", sha256="aba07acdc39a0da73f39f48a8cac915d5b671abc008c123bbe30e6759a2499d2")
    version(
        "0.2.1",
        sha256="9017f95cd0730d858b6782be48291423125f49793aa52875d23c63995ef8ff45",
        expand=False,
        url="https://files.pythonhosted.org/packages/c8/01/f57cd1c1481daa17937aed967e391b5aea0f0d4f4b76e87c7a9f143e46f3/evcouplings-0.2.1-py2.py3-none-any.whl",
    )
    version(
        "20251004",
        commit="c4ac882351efdcb6227252947b71ce48304b81c3",
        git="https://github.com/debbiemarkslab/EVcouplings.git",
        branch="pdb-loading-fixes",
    )
    

    depends_on("py-setuptools", type=("build"))
    depends_on("py-billiard", type=("build", "run"))
    depends_on("py-biopython", type=("build", "run"))
    depends_on("py-bokeh", type=("build", "run"))
    depends_on("py-click", type=("build", "run"))
    depends_on("py-filelock", type=("build", "run"))
    depends_on("py-jinja2", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-msgpack", type=("build", "run"))
    depends_on("py-numba", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-psutil", type=("build", "run"))
    depends_on("py-requests", type=("build", "run"))
    depends_on("py-ruamel-yaml", type=("build", "run"))
    depends_on("py-scikit-learn", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-seaborn", type=("build", "run"))
    depends_on("py-setuptools", type=("build", "run"))
    depends_on("cns-solve", type=("build", "run"))
    depends_on("maxcluster", type=("build", "run"))
    depends_on("psipred", type=("build", "run"))
    depends_on("hmmer", type=("build", "run"))
    depends_on("hh-suite", type=("build", "run"))
    depends_on("plmc precision=single", type=("build", "run"))

# {'billiard': ['0.2.1'], 'biopython>=1.84': ['0.2.1'], 'bokeh': ['0.2.1'], 'click': ['0.2.1'], 'filelock': ['0.2.1'], 'jinja2': ['0.2.1'], 'matplotlib': ['0.2.1'], 'msgpack': ['0.2.1'], 'numba': ['0.2.1'], 'numpy': ['0.2.1'], 'pandas': ['0.2.1'], 'psutil': ['0.2.1'], 'requests': ['0.2.1'], 'ruamel-yaml<0.18': ['0.2.1'], 'scikit-learn': ['0.2.1'], 'scipy': ['0.2.1'], 'seaborn': ['0.2.1'], 'setuptools>=18.2': ['0.2.1']}
