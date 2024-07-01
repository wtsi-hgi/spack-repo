# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyGentropy(PythonPackage):
    """Open Targets python framework for post-GWAS analysis"""

    homepage = "https://github.com/opentargets/gentropy"
    pypi = "gentropy/gentropy-1.4.0-py3-none-any.whl"

    version(
        "1.0.0",
        sha256="04586bcf57b15b719bfef51e71fd38e277b445886c3959460060724c81ce4c66",
        expand=False,
        url="https://files.pythonhosted.org/packages/fc/ca/28657e4e84047424e0a89837e1e644ad98e6e29928137c08b0dee0e1dfbc/gentropy-1.0.0-py3-none-any.whl",
    )
    version(
        "1.1.0",
        sha256="6a4d721d9bcea2ecdd968cd4c996d34a6925231fc064b7772f49c9f441d1b503",
        expand=False,
        url="https://files.pythonhosted.org/packages/22/b8/96a40121431b0621f707a9610fe0fd01c34efbacf3c9487297ac56eafedc/gentropy-1.1.0-py3-none-any.whl",
    )
    version(
        "1.1.1",
        sha256="c4b5fa783223c349a1360d6a150c6814ed151ad2ae28a74160df6c6718359532",
        expand=False,
        url="https://files.pythonhosted.org/packages/37/3c/49378a8561252780790e660a7927b243bdf33f77017e63e4637aae8b3732/gentropy-1.1.1-py3-none-any.whl",
    )
    version(
        "1.2.0",
        sha256="8fa1a4b373ae86da48e576ae10547be76d18a18bb9648158dd47082ec09cfd34",
        expand=False,
        url="https://files.pythonhosted.org/packages/0c/50/930b26eaf176a11aaee6cef9859581e295858c165780d325dbd29a4844cd/gentropy-1.2.0-py3-none-any.whl",
    )
    version(
        "1.3.0",
        sha256="f5e37024964f878bf06b5ec207b4170f5adcd6aa98c8b79923088092fe12b5ab",
        expand=False,
        url="https://files.pythonhosted.org/packages/2d/88/ed653633c90899c0d1e969fa6e6b1f8cdd4b589ea47ce7b4a5307857a636/gentropy-1.3.0-py3-none-any.whl",
    )
    version(
        "1.4.0",
        sha256="3d749bc6f022a747b42167feeb367012bb6bd303aee50fa32b53fd166054a926",
        expand=False,
        url="https://files.pythonhosted.org/packages/f3/e0/fe15e6f9e731a8d8e86924ff09221c3e2d410de2bf1116f8f7070e7961c6/gentropy-1.4.0-py3-none-any.whl",
    )

    depends_on("python@3.10", type=("build", "run"))
    depends_on("py-xgboost", type=("build", "run"))
    depends_on("py-wandb", type=("build", "run"))
    depends_on("py-typing-extensions", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-scikit-learn", type=("build", "run"))
    depends_on("py-pyspark", type=("build", "run"))
    depends_on("py-pyliftover", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-omegaconf", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-hydra-core", type=("build", "run"))
    depends_on("py-hail", type=("build", "run"))
    depends_on("py-google-cloud-secret-manager", type=("build", "run"))
    depends_on("py-google", type=("build", "run"))


# {'google(>=3.0.0,<4.0.0)': ['1.0.0', '1.1.0', '1.1.1', '1.2.0', '1.3.0', '1.4.0'], 'hail(==0.2.127)': ['1.0.0', '1.1.0', '1.1.1', '1.2.0', '1.3.0', '1.4.0'], 'hydra-core(>=1.3.2,<2.0.0)': ['1.0.0', '1.1.0', '1.1.1', '1.2.0', '1.3.0', '1.4.0'], 'numpy(>=1.26.2,<2.0.0)': ['1.0.0', '1.1.0', '1.1.1', '1.2.0', '1.3.0', '1.4.0'], 'omegaconf(>=2.3.0,<3.0.0)': ['1.0.0', '1.1.0', '1.1.1', '1.2.0', '1.3.0', '1.4.0'], 'pandas(>=2.1.4,<3.0.0)': ['1.0.0', '1.1.0', '1.1.1', '1.2.0', '1.3.0'], 'pyliftover(>=0.4,<0.5)': ['1.0.0', '1.1.0', '1.1.1', '1.2.0', '1.3.0', '1.4.0'], 'pyspark(==3.3.4)': ['1.0.0', '1.1.0', '1.1.1', '1.2.0', '1.3.0', '1.4.0'], 'scikit-learn(>=1.3.2,<2.0.0)': ['1.0.0', '1.1.0', '1.1.1', '1.2.0', '1.3.0', '1.4.0'], 'scipy(>=1.11.4,<2.0.0)': ['1.0.0', '1.1.0', '1.1.1', '1.2.0', '1.3.0', '1.4.0'], 'typing-extensions(>=4.9.0,<5.0.0)': ['1.0.0', '1.1.0', '1.1.1', '1.2.0', '1.3.0', '1.4.0'], 'wandb(>=0.16.2,<0.17.0)': ['1.0.0', '1.1.0', '1.1.1', '1.2.0', '1.3.0'], 'xgboost(>=1.7.3,<2.0.0)': ['1.0.0', '1.1.0', '1.1.1', '1.2.0', '1.3.0', '1.4.0'], 'google-cloud-secret-manager(>=2.20.0,<3.0.0)': ['1.4.0'], 'pandas[gcp,parquet](>=2.2.2,<3.0.0)': ['1.4.0'], 'wandb(>=0.16.2,<0.18.0)': ['1.4.0']}
