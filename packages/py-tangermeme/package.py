# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyTangermeme(PythonPackage):
    """Biological sequence analysis for the modern age."""

    homepage = "https://github.com/jmschrei/tangermeme"
    pypi = "tangermeme/tangermeme-1.0.4-py3-none-any.whl"

    license("MIT")

    version("0.0.1", sha256="1f7e3dc22931bc2ed1623bbac3d826cc17ae6cbbfe6b94bf74616b1c1badb0f8", expand=False, url="https://files.pythonhosted.org/packages/a9/e0/853e8caeb0d5f4b8fc911ef2757748fff62b26f2ca856819f98d89fd6b5d/tangermeme-0.0.1-py3-none-any.whl")
    version("0.1.0", sha256="5927021889924818215ead6266c36375bfb53955597133077ce3213992bf4eb8", expand=False, url="https://files.pythonhosted.org/packages/7f/5a/9a9b74932c857fce18dfdeea136beccd406a29bd7d8c4b31ed26db4cde32/tangermeme-0.1.0-py3-none-any.whl")
    version("0.1.0rc0", sha256="0dced710943f03348f92406c9a8614c5783624fc7f3d17a0d6e1cad05ea673a0", expand=False, url="https://files.pythonhosted.org/packages/8f/21/8567311fe56325b390a914dc5d41efd9646e2277857d10c50338c740a7ce/tangermeme-0.1.0rc0-py3-none-any.whl")
    version("0.2.0", sha256="4ac3c42bdf94ec27de7a702a65dd37973b153dfc3df8f04b82ab0a536e916377", expand=False, url="https://files.pythonhosted.org/packages/85/98/8b03de434fb8d1de09875fb9c4e49b67f54d4f819b1932af6e81c50ff58d/tangermeme-0.2.0-py3-none-any.whl")
    version("0.2.1", sha256="8cc8bf17257fb48e8886cd86b7a5c44722647775e965ceb69fb6c37ac836cc60", expand=False, url="https://files.pythonhosted.org/packages/c8/f2/683780a3928ca9487fad8436ff74414a1487a6a59c201e8a5860868613c8/tangermeme-0.2.1-py3-none-any.whl")
    version("0.2.2", sha256="697d9bd0f1f731a6033e1cf22e4a0515282eb98bededad8c7ba6063078be062b", expand=False, url="https://files.pythonhosted.org/packages/af/06/280770a1f6b00b590a29ff0f04da3182000f5b9ab782508b49156ba1beeb/tangermeme-0.2.2-py3-none-any.whl")
    version("0.2.3", sha256="e4bbcfb6e1f1ce1b99231bb809ed118177a7dcbf6056f23b4bbcd12d0059060f", expand=False, url="https://files.pythonhosted.org/packages/6a/df/da3fcc7597bb035b223751c8f4163745a33640f1e5e85e8192cecacfe07c/tangermeme-0.2.3-py3-none-any.whl")
    version("0.3.0", sha256="a3659f99e087d0a4a2368da3f7c82732ddc29006d14f57438af5daa034083385", expand=False, url="https://files.pythonhosted.org/packages/dd/f3/8b88b5fd340277de88323bd32b797ed4b3649235041aaa1c4d0f1a7537e2/tangermeme-0.3.0-py3-none-any.whl")
    version("0.4.0", sha256="84f8852f24c6573c5a511818af5e0d4b8a692e9cefb6654428649f2270745001", expand=False, url="https://files.pythonhosted.org/packages/fb/99/cccc3cdf1eefd65b7382516140706c39cc7fca3eb71e650b777c232e8832/tangermeme-0.4.0-py3-none-any.whl")
    version("0.4.1", sha256="2df271caab3c03d2ccd4fe7c34ce77da33795d3ef3cd390bc4f0e78766f4f1df", expand=False, url="https://files.pythonhosted.org/packages/13/8c/99a4a0b16661de407ab69902f6cbf3557545ce8fd6fc7a440a7b6b7933ee/tangermeme-0.4.1-py3-none-any.whl")
    version("0.4.2", sha256="aede18d5d409f4309312d40a2e47bb36c7e36735c0f90a839012296728f5dc20", expand=False, url="https://files.pythonhosted.org/packages/1c/eb/8e2b41e493cf884ae79036b2e444f32b2bd1f9c7e0cc1580b230e6e11936/tangermeme-0.4.2-py3-none-any.whl")
    version("0.4.3", sha256="548b05e934e11cbeb777c5e6f135a4bec254ee66ba3846760def9e6b1c390403", expand=False, url="https://files.pythonhosted.org/packages/ec/85/274850b249ed4733eef3e086b60187e4df5eb39cc519da32773f443a58de/tangermeme-0.4.3-py3-none-any.whl")
    version("0.4.4", sha256="ad9a5b3889967ee6546fdebf04579c4c1292d65150dc994362811ae65ca18373", expand=False, url="https://files.pythonhosted.org/packages/37/66/4a662c8ace6d2144ebef6523a319138f00aa833344a3c235b7c88f13a5d2/tangermeme-0.4.4-py3-none-any.whl")
    version("0.5.0", sha256="657d5558331170388be94b4d4fd782a9e493ca431f5d82802cc1995acfecb2cc", expand=False, url="https://files.pythonhosted.org/packages/c0/bd/2814b813a0b0a9a61bb04811d5d7197293398a33d70b749a070e59931ca8/tangermeme-0.5.0-py3-none-any.whl")
    version("0.5.1", sha256="4a41f35a53a69e892587f2d618e5042896400edfc6cb9d06c8de2137ac214128", expand=False, url="https://files.pythonhosted.org/packages/c5/76/3e5cd3d44f3e3cd235d6a2c2a26ce03928a11070631775894c325cdabd09/tangermeme-0.5.1-py3-none-any.whl")
    version("1.0.0", sha256="3719a8304b7115eac4f85a7978c4319145a6c7b26cedfc8ea156d79e009f1ade", expand=False, url="https://files.pythonhosted.org/packages/33/3e/a063a7945ec12774cb8222d90e6fcebd6f6a31f1fdac9521ba89dddb1301/tangermeme-1.0.0-py3-none-any.whl")
    version("1.0.2", sha256="e812f256a9b65825a42a2b0b502ab4eaf3e92186cb1232163451ad9978a18ccd", expand=False, url="https://files.pythonhosted.org/packages/0e/d1/071b5872cb790d9d8af7ea5575f827b2c55e3121b191e8074d712bdd00f7/tangermeme-1.0.2-py3-none-any.whl")
    version("1.0.3", sha256="b7070591d4a04505e38b72d6746d0d2b87271b77a2727a24701c53b649557c2a", expand=False, url="https://files.pythonhosted.org/packages/96/d7/b6dd90e0ef5e2e04281e132d3e77fc8387761578cc10567c6c338cbf7235/tangermeme-1.0.3-py3-none-any.whl")
    version("1.0.4", sha256="c5a6b8e7af7b0871fe7912e3fa72d4b19aba06062be9b2de80b1d566851f992f", expand=False, url="https://files.pythonhosted.org/packages/23/81/1409b61fa74eb974dd4cbe4b614d9458f71e7b9a8bf5d02fad079a1a309b/tangermeme-1.0.4-py3-none-any.whl")
    
    depends_on("py-setuptools", type="build")

    with default_args(type=("build", "run")):
        depends_on("python@3.9:")
        depends_on("py-numpy")
        depends_on("py-scipy")
        depends_on("py-pandas")
        depends_on("py-torch~cuda~distributed~rocm")
        depends_on("py-pybigtools")
        depends_on("py-pyfaidx")
        depends_on("py-tqdm")
        depends_on("py-numba")
        depends_on("py-joblib")
        depends_on("py-scikit-learn")
        depends_on("py-matplotlib")
        depends_on("py-memelite")

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python = self.spec["python"].command
            python("-c", "import tangermeme")

# {'numpy>=1.14.2': ['0.0.1', '0.1.0', '0.1.0rc0', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.3.0', '0.4.0', '1.0.3', '1.0.4'], 'scipy>=1.0.0': ['0.0.1', '0.1.0', '0.1.0rc0', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.3.0', '0.4.0', '0.4.1', '0.4.2', '0.4.3', '0.4.4', '0.5.0', '0.5.1', '1.0.0', '1.0.2', '1.0.3', '1.0.4'], 'pandas>=1.3.3': ['0.0.1', '0.1.0', '0.1.0rc0', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.3.0', '0.4.0', '0.4.1', '0.4.2', '0.4.3', '0.4.4', '0.5.0', '0.5.1', '1.0.0', '1.0.2', '1.0.3', '1.0.4'], 'pyBigWig>=0.3.17': ['0.0.1', '0.1.0', '0.1.0rc0', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.3.0', '0.4.0', '0.4.1', '0.4.2', '0.4.3', '0.4.4', '0.5.0', '0.5.1', '1.0.0'], 'torch>=1.9.0': ['0.0.1', '0.1.0', '0.1.0rc0', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.3.0', '0.4.0', '0.4.1', '0.4.2', '0.4.3', '0.4.4', '0.5.0', '0.5.1', '1.0.0', '1.0.2', '1.0.3', '1.0.4'], 'pyfaidx>=0.7.2.1': ['0.0.1', '0.1.0', '0.1.0rc0', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.3.0', '0.4.0', '0.4.1', '0.4.2', '0.4.3', '0.4.4', '0.5.0', '0.5.1', '1.0.0', '1.0.2', '1.0.3', '1.0.4'], 'tqdm>=4.64.1': ['0.0.1', '0.1.0', '0.1.0rc0', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.3.0', '0.4.0', '0.4.1', '0.4.2', '0.4.3', '0.4.4', '0.5.0', '0.5.1', '1.0.0', '1.0.2', '1.0.3', '1.0.4'], 'numba>=0.55.1': ['0.0.1', '0.1.0', '0.1.0rc0', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.3.0', '0.4.0', '0.4.1', '0.4.2', '0.4.3', '0.4.4', '0.5.0', '0.5.1', '1.0.0', '1.0.2', '1.0.3', '1.0.4'], 'logomaker': ['0.0.1', '0.1.0', '0.1.0rc0', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.3.0', '0.4.0', '0.4.1', '0.4.2', '0.4.3', '0.4.4', '0.5.0', '0.5.1', '1.0.0', '1.0.2', '1.0.3'], 'joblib>=1.3.2': ['0.0.1', '0.1.0', '0.1.0rc0', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.3.0', '0.4.0', '0.4.1', '0.4.2', '0.4.3', '0.4.4', '0.5.0', '0.5.1', '1.0.0', '1.0.2', '1.0.3', '1.0.4'], 'scikit-learn>=1.2.2': ['0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.3.0', '0.4.0', '0.4.1', '0.4.2', '0.4.3', '0.4.4', '0.5.0', '0.5.1', '1.0.0', '1.0.2', '1.0.3', '1.0.4'], 'matplotlib': ['0.4.0', '0.4.1', '0.4.2', '0.4.3', '0.4.4', '0.5.0', '0.5.1', '1.0.0', '1.0.2', '1.0.3', '1.0.4'], 'numpy<=2.0.1,>=1.14.2': ['0.4.1', '0.4.2', '0.4.3', '0.4.4', '0.5.0', '0.5.1', '1.0.0', '1.0.2'], 'memelite': ['0.5.0', '0.5.1', '1.0.0', '1.0.2', '1.0.3', '1.0.4'], 'pybigtools': ['1.0.0', '1.0.2', '1.0.3', '1.0.4']}
