# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyMarisaTrie(PythonPackage):
    """Static memory-efficient and fast Trie-like structures for Python."""
    
    homepage = "https://marisa-trie.readthedocs.io/en/latest/"
    pypi = "marisa-trie/marisa_trie-1.3.1.tar.gz"

    license("MIT")

    version("0.1", sha256="c8125d63e37942d7cf714d68e37e43ba4bb0137bf42841b838f7de04bd17d278")
    version("0.2", sha256="6f570fc4250d47ccf80d8d18cb4d11fa6d3d8f07bab4ffcd9d254561a8cf18de")
    version("0.3", sha256="cf786681dbe1caf275c75cff0956f162892aba94a79af6c62c40d40f77596a61")
    version("0.3.1", sha256="ba0c205a595ffdad1e18fd6ee07f70ccd0cb4e2f06109ca6029e94c0378f26d1")
    version("0.3.2", sha256="b9905e7d7ad5c611ad7b12ab90e87647313a3f4d294c7b2c27aac9b71b8e7020")
    version("0.3.3", sha256="b3ab0e0ad93813f3a4e0f7c59568ee6f78db585b63913a857b3ae60d0e6ac385")
    version("0.3.4", sha256="5ab975cd71fe60ec976f806c4c1e5805b706696390dc874444594808020e6b89")
    version("0.3.5", sha256="fc23a421d451f219a293bda9a2fae14059031dfac286c8f247cddf240c2c22f1")
    version("0.3.6", sha256="77e7577a60f2f5ca4e2d29fe247e17b123c87ce3b5574daa6f775cfd7cd19047")
    version("0.3.7", sha256="f3d9dc8b0341ea409339079d00247f35b174211fde0ef19bf761641ee877078e")
    version("0.3.8", sha256="8d30549d168a764af7ced5020653d89a3df39a08462168f8d203513a1c3102d3")
    version("0.4", sha256="1ba3f976dc55e4a133ebda278389f4446cd4ecab4fb4e133ee9ddc63b59f8602")
    version("0.5", sha256="7463f19af2dcbbe91df7909cff5385ed1f8c11c218de15075157e9ffe923f6ac")
    version("0.5.1", sha256="10e57ef0fdc4b8684e476d802624b4b3d5546d4f6fc6cf8e6d935a9a7f49557b")
    version("0.5.2", sha256="7fa92c8af24508584c5d7bfa74f95b4db980fcca53e91785498aa5c5f83f8ef1")
    version("0.5.3", sha256="863d5cad1a2c47582434ff647d46416de59bba9d3c9c60f323a98a780aaa3b7b")
    version("0.6", sha256="ba4f35c95d4393626c25b47a5d0b4216cee0a7cccb67e13e7e809bef3867b9d2")
    version("0.7", sha256="59c7bf495b5aec76574dd0b796d96dd3a1de20ac611e9e60f440a0e9cbc8ffcb")
    version("0.7.1", sha256="2a6842d6f74c5ccefc8590d0ab48afb57672dd82ee6493948d6259886e83018a")
    version("0.7.2", sha256="4b39f84c511a6e8e3a060b20bc41ff3b5393cb46381336e2156dc9b2290506b3")
    version("0.7.4-py26", sha256="dd1b5464d7ea2eb54758dcde40385d12e75cf74f6a44d27459ccb8c282ebc8c8", expand=False, url="https://files.pythonhosted.org/packages/64/58/899be44adfbbc2e701aec9af82fbbc11b4f7ad8330236d8e6049653b6ed7/marisa_trie-0.7.4-cp26-cp26mu-manylinux1_x86_64.whl")
    version("0.7.4-py27", sha256="89bd183e0f75357f074658492bb24a4bbac8e1a13fd0f54553017c122eeef134", expand=False, url="https://files.pythonhosted.org/packages/27/8c/c8d95695002364b8bb203d786de754be9bde566e5c00efa00941874e508b/marisa_trie-0.7.4-cp27-cp27mu-manylinux1_x86_64.whl")
    version("0.7.4-py34", sha256="ef381b579aee59098652a5fe5b5d9a93f4c93b21cd74d825fbb84c4447c21d83", expand=False, url="https://files.pythonhosted.org/packages/59/c9/0b9c3206d018737d712e7e37e44a1926f0d2dae3080837925b24ddab1b12/marisa_trie-0.7.4-cp34-cp34m-manylinux1_x86_64.whl")
    version("0.7.4-py35", sha256="accdaedcb86bac8fd6748c99dd577dd65a76026872bb5873626f3f401f57a043", expand=False, url="https://files.pythonhosted.org/packages/d3/2a/3d64c70eaaf0dbd896b88ce46d9a7da0f2f7b59deee03ea3155b0eab46a6/marisa_trie-0.7.4-cp35-cp35m-manylinux1_x86_64.whl")
    version("0.7.4-py36", sha256="32cbf5d5a6630e8bd6015fa7600f3e076bc321bf9768e6d4d41e751004ff6657", expand=False, url="https://files.pythonhosted.org/packages/1b/5f/21295ebb1feb1abde1e7652c0a4c182b4c25bdd5dda5a0f5b34d4e88bcc3/marisa_trie-0.7.4-cp36-cp36m-manylinux1_x86_64.whl")
    version("0.7.5", sha256="c73bc25d868e8c4ea7aa7f1e19892db07bba2463351269b05340ccfa06eb2baf")
    version("0.7.6", sha256="f20c084dc916d30da56d770f83945a9a8e5362161c9be43881b5f7d81e325010")
    version("0.7.7", sha256="bbeafb7d92839dc221365340e79d012cb50ee48a1f3f30dd916eb35a8b93db00")
    version("0.7.8", sha256="aee3de5f2836074cfd803f1caf16f68390f262ef09cd7dc7d0e8aee9b6878643")
    version("0.8.0", sha256="3d019d17b0d7f62d6e6d7bd05236d8252624ea1c140beb8bf9c6eeff38b3c707")
    version("1.0.0", sha256="d8a68301f023a724eb379aaa1b10f88a9e1a458cc8a41b527c62507859b4a4d2")
    version("1.1.0", sha256="5bf43ed0cf36af4578fe7b034cf95f532439766516680e4bd603723611ebd56b")
    version("1.1.1", sha256="363f1be2314b1f9e26b5a3de45b59fd9a0a3289bf157be61bbed770643a46f1a")
    version("1.2.0", sha256="fedfc67497f8aa2757756b5cf493759f245d321fb78914ce125b6d75daa89b5f")
    version("1.2.1", sha256="3a27c408e2aefc03e0f1d25b2ff2afb85aac3568f6fa2ae2a53b57a2e87ce29d")
    version("1.3.0", sha256="39af3060b4ab41a3cce18b1808338db8bf50b6ec4b81be3cc452558aaad95581")
    version("1.3.1", sha256="97107fd12f30e4f8fea97790343a2d2d9a79d93697fe14e1b6f6363c984ff85b", preferred=True)
    version("1.3.2.dev0", sha256="0c1f80ca0c0e70cf78f25fc92270134476b7949a51ca377b2e1590baf3a07f25")

    depends_on("py-setuptools", type=("build"))
    depends_on("py-cython", type=("build"))
    depends_on("python@3.9:", type=("build", "run"))
    depends_on("python@2.6", when="@0.7.4-py26", type=("build", "run"))
    depends_on("python@2.7", when="@0.7.4-py27", type=("build", "run"))
    depends_on("python@3.4", when="@0.7.4-py34", type=("build", "run"))
    depends_on("python@3.5", when="@0.7.4-py35", type=("build", "run"))
    depends_on("python@3.6", when="@0.7.4-py36", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            # No CLI; verify Python import succeeds
            python("-c", "import marisa_trie")

    def patch(self):
        # Upstream pyproject.toml contains duplicated tables and an SPDX-style
        # license string that setuptools 68 misinterprets. Normalize for build.
        # Restrict to known affected release(s).
        if self.spec.satisfies("@1.3.1"):
            # Work around upstream duplicated pyproject metadata by removing file
            # so build falls back to legacy setup.py which works with Spack.
            import os
            if os.path.exists("pyproject.toml"):
                os.remove("pyproject.toml")
