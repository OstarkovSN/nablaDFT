import sys

from setuptools import find_packages, setup


def get_python_version():
    version_info = sys.version_info
    major = version_info[0]
    minor = version_info[1]
    return f"cp{major}{minor}"


PYTHON_VERSION = get_python_version()


setup(
    name="nablaDFT",
    version="2.0.0alpha",
    author="Khrabrov, Kuzma  and Ber, Anton and Tsypin, Artem and Ushenin, Konstantin and Rumiantsev, Egor"
    "and Telepov, Alexander and Protasov, Dmitry and Shenbin, Ilya and Alekseev, Anton"
    "and Shirokikh, Mikhail and Nikolenko, Sergey and Tutubalina, Elena and Kadurin, Artur",
    url="https://github.com/AIRI-Institute/nablaDFT",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=[],
    license="MIT",
    description="$\nabla^2$ DFT: A Universal Quantum Chemistry Dataset of Drug-Like Molecules"
    "and a Benchmark for Neural Network Potentials",
    long_description="""Methods of computational quantum chemistry provide accurate approximations of molecular 
    properties crucial for computer-aided drug discovery and other areas of chemical science. However, 
    high computational complexity limits the scalability of their applications. Neural network potentials (NNPs) are 
    a promising alternative to quantum chemistry methods, but they require large and diverse datasets for training. 
    This work presents a new dataset and benchmark called $\nabla^2$ DFT that is based on the nablaDFT. It contains 
    twice as much molecular structures, three times more conformations, new data types and tasks, 
    and state-of-the-art models. The dataset includes energies, forces, 17 molecular properties, Hamiltonian and 
    overlap matrices, and a wavefunction object. All calculations were performed at the DFT level (ωB97X-D/def2-SVP) 
    for each conformation. Moreover, $\nabla^2$ DFT is the first dataset that contains relaxation trajectories for a 
    substantial number of drug-like molecules. We also introduce a novel benchmark for evaluating NNPs in molecular 
    property prediction, Hamiltonian prediction, and conformational optimization tasks.""",
    classifiers=[
        "Development Status :: 4 - Beta",
    ],
)
