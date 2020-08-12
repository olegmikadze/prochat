const { Sequelize  } = require('sequelize');

const sequelize = new Sequelize('prochat', 'postgres', '1', {
    host: 'localhost',
    dialect: 'postgres'
});

try {
    sequelize.authenticate();
} catch (error) {
    console.error('Unable to connect to the database:', error);
}

module.exports = sequelize;