# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyQuickdraws(PythonPackage):
    """Quickdraws is a software tool for performing Genome-Wide Association Studies (GWAS)"""

    homepage = "None"
    pypi = "quickdraws/quickdraws-0.0.3-py3-none-any.whl"

    version(
        "0.0.1",
        sha256="2fd0f452b8a7cae64ec7405317deab42917533641efab4bd8d425c0f581ea648",
        expand=False,
        url="https://files.pythonhosted.org/packages/4a/a0/dd772c179d4c057fe9d825959c99c9df1851c442d22e182af301791833ae/quickdraws-0.0.1-py3-none-any.whl",
    )
    version(
        "0.0.2",
        sha256="990b9af2ad23d55ce7667a083fdf7256b066a3fbfb0841107fa27612b9c742ee",
        expand=False,
        url="https://files.pythonhosted.org/packages/ab/d8/8a2a2a309df25faeb9c8521c30f7e050efbca9ebdd288c6fdf863f449c4d/quickdraws-0.0.2-py3-none-any.whl",
    )
    version(
        "0.0.3",
        sha256="be0b952830c32df2aa08d0e997a708f8ec3399b7bc06fc95faf9952cc56faf90",
        expand=False,
        url="https://files.pythonhosted.org/packages/8c/78/0ce94c805f12db8d792ac5183fc9ea9c982b26a28b452998eed1a8ecbae6/quickdraws-0.0.3-py3-none-any.whl",
    )

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-torch", type=("build", "run"))
    depends_on("py-rhe", type=("build", "run"))
    depends_on("py-pybgen", type=("build", "run"))
    depends_on("py-bitsandbytes", type=("build", "run"))
    depends_on("py-tables", type=("build", "run"))
    depends_on("py-wandb", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-statsmodels", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-scikit-learn", type=("build", "run"))
    depends_on("py-pysnptools+bgen", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-numba@0.58:", type=("build", "run"))
    depends_on("py-joblib", type=("build", "run"))
    depends_on("py-h5py", type=("build", "run"))


# {'bitsandbytes': ['0.0.1', '0.0.2', '0.0.3'], 'h5py': ['0.0.1', '0.0.2', '0.0.3'], 'joblib': ['0.0.1', '0.0.2', '0.0.3'], 'numba': ['0.0.1', '0.0.2', '0.0.3'], 'numpy(<2)': ['0.0.1', '0.0.2', '0.0.3'], 'pandas': ['0.0.1', '0.0.2', '0.0.3'], 'pybgen': ['0.0.1', '0.0.2', '0.0.3'], 'pysnptools[bgen]': ['0.0.1', '0.0.2', '0.0.3'], 'rhe(==1.0.0)': ['0.0.1', '0.0.2', '0.0.3'], 'scikit_learn': ['0.0.1', '0.0.2', '0.0.3'], 'scipy': ['0.0.1', '0.0.2', '0.0.3'], 'statsmodels': ['0.0.1', '0.0.2', '0.0.3'], 'tables': ['0.0.1', '0.0.2', '0.0.3'], 'torch(==2.*)': ['0.0.1', '0.0.2', '0.0.3'], 'tqdm': ['0.0.1', '0.0.2', '0.0.3'], 'wandb': ['0.0.1', '0.0.2', '0.0.3']}
